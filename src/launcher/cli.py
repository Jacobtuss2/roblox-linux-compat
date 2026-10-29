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
        self.profile_dir = Path(profile_dir) if profile_dir else self.home / ".roblox-linux-compat" / "profiles"
        self.prefix = Path(prefix) if prefix else self.home / ".roblox-linux-compat"
        self.override_exe = Path(exe) if exe else None
        self.env = {
            "WINEPREFIX": str(self.prefix),
            "WINEDLLOVERRIDES": "winemenubuilder.exe=d",
            "DXVK_ASYNC": "1",
            "VKD3D_CONFIG": "dxr,dxr11",
        }

    def _profile_paths(self) -> list[Path]:
        candidates = [
            self.profile_dir / f"{self.profile_name}.json",
            self.home / ".roblox-linux-compat" / "profiles" / f"{self.profile_name}.json",
            Path(__file__).resolve().parents[2] / "profiles" / f"{self.profile_name}.json",
        ]
        return [p for p in candidates if p.exists()]

    def load_profile(self, profile_name: str | None = None) -> dict:
        name = profile_name or self.profile_name
        self.profile_name = name
        profile_paths = [
            self.profile_dir / f"{name}.json",
            self.home / ".roblox-linux-compat" / "profiles" / f"{name}.json",
            Path(__file__).resolve().parents[2] / "profiles" / f"{name}.json",
        ]
        for path in profile_paths:
            if path.exists():
                with open(path, "r", encoding="utf-8") as fh:
                    data = json.load(fh)
                if "prefix" in data:
                    self.prefix = Path(data["prefix"]).expanduser()
                if "exe" in data:
                    self.override_exe = Path(data["exe"]).expanduser()
                if "env" in data:
                    self.env.update({str(k): str(v) for k, v in data["env"].items()})
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
