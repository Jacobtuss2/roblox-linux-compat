#!/usr/bin/env bash
set -euo pipefail

export WINEPREFIX="${WINEPREFIX:-$HOME/.roblox-linux-compat}"
export WINEDLLOVERRIDES="${WINEDLLOVERRIDES:-winemenubuilder.exe=d}"
export DXVK_ASYNC="${DXVK_ASYNC:-1}"
export VKD3D_CONFIG="${VKD3D_CONFIG:-dxr,dxr11}"

if [ -z "${1:-}" ]; then
  echo "Usage: $0 /path/to/RobloxInstaller.exe"
  exit 1
fi

INSTALLER="$1"

if [ ! -f "$INSTALLER" ]; then
  echo "Installer not found: $INSTALLER"
  exit 2
fi

mkdir -p "$WINEPREFIX"

if ! command -v wine >/dev/null 2>&1; then
  echo "wine is not installed or is missing from PATH."
  exit 1
fi

echo "Launching Roblox installer inside Wine prefix: $WINEPREFIX"
wine "$INSTALLER"

echo "Roblox installation has been attempted."
echo "Verify the launcher exists at one of:"
echo "  $WINEPREFIX/drive_c/Program Files/Roblox/RobloxPlayerLauncher.exe"
echo "  $WINEPREFIX/drive_c/Program Files (x86)/Roblox/RobloxPlayerLauncher.exe"
