import os
import subprocess
from pathlib import Path


class RuntimeDiagnostics:
    def __init__(self, prefix: Path | None = None):
        self.prefix = prefix or Path.home() / ".roblox-linux-compat"

    def collect(self):
        info = []
        info.append("Wine prefix: " + str(self.prefix))
        info.append("Wine version: " + subprocess.getoutput("wine --version"))
        info.append("Vulkan info: " + subprocess.getoutput("vulkaninfo | head -20"))
        info.append("Prefix listing: " + subprocess.getoutput(f"ls -R {self.prefix} | head -50"))
        return "\n".join(info)

    def save(self, output_path: str = "/tmp/roblox-diagnostics.txt"):
        report = self.collect()
        with open(output_path, "w", encoding="utf-8") as fh:
            fh.write(report)
        return output_path
