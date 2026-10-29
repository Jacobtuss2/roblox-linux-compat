#!/usr/bin/env bash
set -euo pipefail

export WINEPREFIX="${WINEPREFIX:-$HOME/.roblox-linux-compat}"
export WINEDLLOVERRIDES="${WINEDLLOVERRIDES:-winemenubuilder.exe=d}"
export DXVK_ASYNC="${DXVK_ASYNC:-1}"
export VKD3D_CONFIG="${VKD3D_CONFIG:-dxr,dxr11}"

echo "Collecting Roblox compatibility diagnostics..."
echo "Wine prefix: $WINEPREFIX"

if command -v wine >/dev/null 2>&1; then
  wine --version || true
else
  echo "wine is not installed or not on PATH"
fi

if [ -f "$WINEPREFIX/drive_c/Program Files/Roblox/RobloxPlayerLauncher.exe" ]; then
  echo "Attempting launch to capture startup errors..."
  wine "$WINEPREFIX/drive_c/Program Files/Roblox/RobloxPlayerLauncher.exe" 2>&1 | tee "$HOME/roblox-debug.log"
else
  echo "Roblox launcher was not found."
  echo "Install Roblox first, or check the Wine prefix at: $WINEPREFIX"
fi
