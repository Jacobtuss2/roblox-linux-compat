import subprocess
from pathlib import Path


class RuntimeDiagnostics:
    def __init__(self, prefix: str | Path | None = None):
        self.prefix = Path(prefix) if prefix is not None else Path.home() / ".roblox-linux-compat"

    def _roblox_launcher_candidates(self) -> list[Path]:
        return [
            self.prefix / "drive_c" / "Program Files" / "Roblox" / "RobloxPlayerLauncher.exe",
            self.prefix / "drive_c" / "Program Files (x86)" / "Roblox" / "RobloxPlayerLauncher.exe",
            self.prefix / "drive_c" / "Program Files" / "Roblox Player" / "RobloxPlayerLauncher.exe",
        ]

    def collect(self) -> str:
        launcher = next((p for p in self._roblox_launcher_candidates() if p.exists()), self._roblox_launcher_candidates()[0])

        info = []
        info.append(f"Wine prefix: {self.prefix}")
        info.append(f"Wine version: {subprocess.getoutput('wine --version 2>/dev/null || echo unavailable')}")
        info.append(f"Wine config: {subprocess.getoutput('winecfg --help 2>/dev/null | head -1 || echo unavailable')}")
        info.append(f"Vulkan info: {subprocess.getoutput('vulkaninfo 2>/dev/null | head -20 || echo unavailable')}")
        info.append(f"Prefix exists: {'yes' if self.prefix.exists() else 'no'}")
        info.append(f"Roblox launcher candidate: {launcher}")
        info.append(f"Prefix listing: {subprocess.getoutput(f'ls -R {self.prefix} 2>/dev/null | head -50 || echo unavailable')}")
        return "\n".join(info)

    def save(self, output_path: str = "/tmp/roblox-diagnostics.txt") -> str:
        report = self.collect()
        with open(output_path, "w", encoding="utf-8") as fh:
            fh.write(report)
        return output_path
