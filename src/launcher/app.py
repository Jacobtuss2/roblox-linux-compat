import os
import shutil
import subprocess
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from launcher.config import RobloxConfig


class RobloxLauncher:
    def __init__(self, config: RobloxConfig | None = None):
        self.config = config or RobloxConfig()

    def ensure_runtime(self) -> tuple[bool, str]:
        if shutil.which("wine") is None:
            return False, "wine is not installed or not on PATH."

        if not self.config.prefix.exists():
            return False, f"Wine prefix does not exist: {self.config.prefix}"

        exe = self.config.get_roblox_exe()
        if not exe.exists():
            return False, f"Roblox launcher not found: {exe}"

        return True, "Runtime is ready."

    def run(self) -> int:
        ok, message = self.ensure_runtime()
        if not ok:
            print(f"[roblox-linux-compat] {message}")
            print("Install the system dependencies, initialize the Wine prefix, and install Roblox before retrying.")
            return 1

        env = self.config.build_env()
        exe = self.config.get_roblox_exe()

        print(f"[roblox-linux-compat] Launching Roblox via Wine: {exe}")
        try:
            return subprocess.call(["wine", str(exe)], env=env)
        except FileNotFoundError:
            print("[roblox-linux-compat] wine command not found.")
            return 1


if __name__ == "__main__":
    sys.exit(RobloxLauncher().run())
