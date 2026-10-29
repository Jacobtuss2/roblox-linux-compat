import os
import subprocess
import sys
from pathlib import Path


class RuntimeRunner:
    def __init__(self, prefix: Path | None = None):
        self.prefix = prefix or Path.home() / ".roblox-linux-compat"

    def launch(self, exe_path: str | None = None):
        target = exe_path or str(self.prefix / "drive_c" / "Program Files" / "Roblox" / "RobloxPlayerLauncher.exe")
        env = os.environ.copy()
        env["WINEPREFIX"] = str(self.prefix)
        env["DXVK_ASYNC"] = "1"
        env["VKD3D_CONFIG"] = "dxr,dxr11"
        env["WINEDLLOVERRIDES"] = "winemenubuilder.exe=d"

        return subprocess.call(["wine", target], env=env)
