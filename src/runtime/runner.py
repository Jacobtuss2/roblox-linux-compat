import os
import subprocess
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from launcher.config import RobloxConfig


class RuntimeRunner:
    def __init__(self, prefix: str | Path | None = None):
        self.config = RobloxConfig(prefix)

    def launch(self, exe_path: str | Path | None = None):
        env = self.config.build_env()

        target = Path(exe_path) if exe_path else self.config.get_roblox_exe()
        if not target.exists():
            raise FileNotFoundError(f"Roblox launcher not found: {target}")

        return subprocess.call(["wine", str(target)], env=env)


if __name__ == "__main__":
    try:
        raise SystemExit(RuntimeRunner().launch())
    except FileNotFoundError as exc:
        print(f"[roblox-linux-compat] {exc}")
        raise SystemExit(1)
