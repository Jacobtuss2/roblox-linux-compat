#!/usr/bin/env bash
set -e

export WINEPREFIX="$HOME/.roblox-linux-compat"
export WINEDLLOVERRIDES="winemenubuilder.exe=d"
export DXVK_ASYNC=1
export VKD3D_CONFIG="dxr,dxr11"

ROBLOX_EXE="$HOME/.roblox-linux-compat/drive_c/Program Files/Roblox/RobloxPlayerLauncher.exe"

if [ ! -f "$ROBLOX_EXE" ]; then
  echo "Roblox launcher not found at $ROBLOX_EXE"
  echo "Install Roblox first or fix your Wine prefix."
  exit 1
fi

echo "Launching Roblox through compatibility runtime..."
wine "$ROBLOX_EXE"
