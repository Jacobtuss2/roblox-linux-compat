#!/usr/bin/env python3
import json
import os
import shutil
from pathlib import Path


class RobloxConfig:
    DEFAULT_PROFILE = "default"

    def __init__(
        self,
        prefix: str | Path | None = None,
        profile_name: str = DEFAULT_PROFILE,
        exe: str | Path | None = None,
        profile_dir: str | Path | None = None,
    ):
        self.home = Path.home()
        self.profile_name = profile_name
        self.profile_dir = Path(profile_dir).expanduser() if profile_dir else self.home / ".roblox-linux-compat" / "profiles"
        self.prefix = self._expand_path(prefix) if prefix else self.home / ".roblox-linux-compat"
        self.override_exe = self._expand_path(exe) if exe else None
        self.env = {
            "WINEPREFIX": str(self.prefix),
            "WINEDLLOVERRIDES": "winemenubuilder.exe=d",
            "DXVK_ASYNC": "1",
            "VKD3D_CONFIG": "dxr,dxr11",
        }

    @staticmethod
    def _expand_path(value: str | Path | None) -> Path | None:
        if value is None:
            return None
        expanded = os.path.expandvars(os.path.expanduser(str(value)))
        return Path(expanded)

    def _candidate_profile_files(self, profile_name: str) -> list[Path]:
        repo_root = Path(__file__).resolve().parents[2]
        return [
            self.profile_dir / f"{profile_name}.json",
            self.home / ".roblox-linux-compat" / "profiles" / f"{profile_name}.json",
            repo_root / "profiles" / f"{profile_name}.json",
        ]

    def load_profile(self, profile_name: str | None = None) -> dict:
        profile_key = profile_name or self.profile_name
        self.profile_name = profile_key
        for path in self._candidate_profile_files(profile_key):
            if not path.exists():
                continue
            with open(path, "r", encoding="utf-8") as fh:
                data = json.load(fh)
            if "prefix" in data:
                self.prefix = self._expand_path(data["prefix"]) or self.prefix
            if "exe" in data:
                self.override_exe = self._expand_path(data["exe"]) or self.override_exe
            if "env" in data:
                for key, value in data["env"].items():
                    self.env[str(key)] = str(value)
            if "WINEPREFIX" in self.env:
                self.prefix = self._expand_path(self.env["WINEPREFIX"]) or self.prefix
            return data
        return {}

    def build_env(self) -> dict[str, str]:
        env = os.environ.copy()
        env.update(self.env)
        return env

    def candidate_paths(self) -> list[Path]:
        if self.override_exe:
            return [self.override_exe]
        return [
            self.prefix / "drive_c" / "Program Files" / "Roblox" / "RobloxPlayerLauncher.exe",
            self.prefix / "drive_c" / "Program Files (x86)" / "Roblox" / "RobloxPlayerLauncher.exe",
            self.prefix / "drive_c" / "Program Files" / "Roblox Player" / "RobloxPlayerLauncher.exe",
        ]

    def get_roblox_exe(self) -> Path:
        for candidate in self.candidate_paths():
            if candidate.exists():
                return candidate
        return self.candidate_paths()[0]

    def validate(self) -> tuple[bool, list[str]]:
        issues: list[str] = []

        if not self.prefix.exists():
            issues.append(f"Wine prefix does not exist: {self.prefix}")

        if not shutil.which("wine"):
            issues.append("wine is not installed or is not on PATH")

        exe = self.get_roblox_exe()
        if not exe.exists():
            issues.append(f"Roblox launcher not found at expected location: {exe}")

        return (len(issues) == 0), issues
