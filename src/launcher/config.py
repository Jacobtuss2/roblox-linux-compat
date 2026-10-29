import os
from pathlib import Path


class RobloxConfig:
    def __init__(self):
        self.home = Path.home()
        self.prefix = self.home / ".roblox-linux-compat"
        self.env = {
            "WINEPREFIX": str(self.prefix),
            "WINEDLLOVERRIDES": "winemenubuilder.exe=d",
            "DXVK_ASYNC": "1",
            "VKD3D_CONFIG": "dxr,dxr11",
        }

    def get_roblox_exe(self):
        return self.prefix / "drive_c" / "Program Files" / "Roblox" / "RobloxPlayerLauncher.exe"
