#!/usr/bin/env python3
import argparse
import os
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
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("launch", help="Launch Roblox through the Wine compatibility stack")
    subparsers.add_parser("status", help="Validate Wine and Roblox installation state")
    subparsers.add_parser("diagnose", help="Collect runtime diagnostics")
    return parser


def handle_status(prefix: str) -> int:
    config = RobloxConfig(prefix)
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
    content = diagnostics.collect()
    print(content)
    return 0


def handle_launch(prefix: str) -> int:
    launcher = RobloxLauncher(RobloxConfig(prefix))
    return launcher.run()


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "launch":
        return handle_launch(args.prefix)
    if args.command == "status":
        return handle_status(args.prefix)
    if args.command == "diagnose":
        return handle_diagnose(args.prefix)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
