#!/usr/bin/env bash
set -euo pipefail

export WINEPREFIX="${WINEPREFIX:-$HOME/.roblox-linux-compat}"
export WINEDLLOVERRIDES="${WINEDLLOVERRIDES:-winemenubuilder.exe=d}"
export DXVK_ASYNC="${DXVK_ASYNC:-1}"
export VKD3D_CONFIG="${VKD3D_CONFIG:-dxr,dxr11}"

ROBLOX_EXE="${ROBLOX_EXE:-$WINEPREFIX/drive_c/Program Files/Roblox/RobloxPlayerLauncher.exe}"

if ! command -v wine >/dev/null 2>&1; then
  echo "wine is not installed or is missing from PATH."
  exit 1
fi

if [ ! -f "$ROBLOX_EXE" ]; then
  echo "Roblox launcher not found at: $ROBLOX_EXE"
  echo "Install Roblox first or confirm the Wine prefix is correct."
  exit 1
fi

echo "Launching Roblox through compatibility runtime..."
exec wine "$ROBLOX_EXE"
