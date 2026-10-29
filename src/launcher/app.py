import os
import subprocess
import sys
from pathlib import Path

from launcher.config import RobloxConfig

class RobloxLauncher:
    def __init__(self):
        self.config = RobloxConfig()

    def ensure_prefix(self):
        self.config.prefix.mkdir(parents=True, exist_ok=True)
        return self.config.get_roblox_exe().exists()

    def run(self):
        if not self.ensure_prefix():
            print("Roblox runtime is not installed in the Wine prefix yet.")
            print("Install Roblox first, then re-run this launcher.")
            return 1

        env = os.environ.copy()
        env.update(self.config.env)

        exe = self.config.get_roblox_exe()
        print(f"Launching Roblox via Wine: {exe}")
        return subprocess.call(["wine", str(exe)], env=env)

if __name__ == "__main__":
    sys.exit(RobloxLauncher().run())
