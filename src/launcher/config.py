#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from launcher.app import RobloxLauncher
from launcher.config import RobloxConfig
from runtime.diagnostics import RuntimeDiagnostics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Roblox Linux compatibility launcher for Raspberry Pi 5")
    parser.add_argument("--prefix", type=str, default=str(Path.home() / ".roblox-linux-compat"), help="Wine prefix path")
    parser.add_argument("--exe", type=str, default=None, help="Explicit path to RobloxPlayerLauncher.exe")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("launch", help="Launch Roblox through the Wine compatibility stack")
    subparsers.add_parser("status", help="Validate Wine and Roblox installation state")
    subparsers.add_parser("diagnose", help="Collect runtime diagnostics")
    return parser


def handle_status(prefix: str, exe_override: str | None) -> int:
    config = RobloxConfig(prefix)
    if exe_override:
        config.override_exe = Path(exe_override)
    ok, issues = config.validate()
    if ok:
        print("[roblox-linux-compat] Runtime status: OK")
        print(f"Wine prefix: {config.prefix}")
        print(f"Launcher: {config.get_roblox_exe()}")
        return 0

    print("[roblox-linux-compat] Runtime status: FAIL")
    for issue in issues:
        print(f"- {issue}")
    return 1


def handle_diagnose(prefix: str) -> int:
    diagnostics = RuntimeDiagnostics(prefix)
    report = diagnostics.collect()
    output_path = diagnostics.save()
    print(report)
    print(f"\n[roblox-linux-compat] Diagnostics saved to: {output_path}")
    return 0


def handle_launch(prefix: str, exe_override: str | None) -> int:
    config = RobloxConfig(prefix)
    if exe_override:
        config.override_exe = Path(exe_override)
    launcher = RobloxLauncher(config)
    return launcher.run()


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "launch":
        return handle_launch(args.prefix, args.exe)
    if args.command == "status":
        return handle_status(args.prefix, args.exe)
    if args.command == "diagnose":
        return handle_diagnose(args.prefix)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
