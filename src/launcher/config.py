import os
import shutil
from pathlib import Path


class RobloxConfig:
    def __init__(self, prefix: str | Path | None = None):
        self.home = Path.home()
        self.prefix = Path(prefix) if prefix is not None else self.home / ".roblox-linux-compat"

    def build_env(self) -> dict[str, str]:
        env = os.environ.copy()
        env.update({
            "WINEPREFIX": str(self.prefix),
            "WINEDLLOVERRIDES": "winemenubuilder.exe=d",
            "DXVK_ASYNC": "1",
            "VKD3D_CONFIG": "dxr,dxr11",
        })
        return env

    def candidate_paths(self) -> list[Path]:
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
