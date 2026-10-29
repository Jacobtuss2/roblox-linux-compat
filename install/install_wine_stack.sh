#!/usr/bin/env bash
set -euo pipefail

export WINEPREFIX="${WINEPREFIX:-$HOME/.roblox-linux-compat}"
export WINEDLLOVERRIDES="${WINEDLLOVERRIDES:-winemenubuilder.exe=d}"
export DXVK_ASYNC="${DXVK_ASYNC:-1}"
export VKD3D_CONFIG="${VKD3D_CONFIG:-dxr,dxr11}"

mkdir -p "$WINEPREFIX"

if ! command -v wine >/dev/null 2>&1; then
  echo "wine is not installed or is missing from PATH."
  exit 1
fi

wineboot --init

if command -v winetricks >/dev/null 2>&1; then
  winetricks corefonts vcrun2022 dxvk vkd3d
else
  echo "winetricks is not installed; install it with the dependency script first."
fi

echo "Wine compatibility runtime is ready."
echo "Install Roblox with: ./src/scripts/install_roblox.sh /path/to/RobloxInstaller.exe"
