#!/usr/bin/env bash
set -e

echo "Collecting Roblox compatibility diagnostics..."

echo "Wine prefix: $HOME/.roblox-linux-compat"

export WINEPREFIX="$HOME/.roblox-linux-compat"
export WINEDLLOVERRIDES="winemenubuilder.exe=d"
export DXVK_ASYNC=1
export VKD3D_CONFIG="dxr,dxr11"

wine --version || true
winecfg || true

ROBLOX_EXE="$HOME/.roblox-linux-compat/drive_c/Program Files/Roblox/RobloxPlayerLauncher.exe"
if [ -f "$ROBLOX_EXE" ]; then
  echo "Attempting launch to capture failures..."
  wine "$ROBLOX_EXE" 2>&1 | tee "$HOME/roblox-debug.log"
else
  echo "Roblox launcher was not found."
  echo "Install Roblox first."
fi
