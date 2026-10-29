#!/usr/bin/env bash
set -e

export WINEPREFIX="$HOME/.roblox-linux-compat"
export WINEDLLOVERRIDES="winemenubuilder.exe=d"
export DXVK_ASYNC=1
export VKD3D_CONFIG="dxr,dxr11"

if [ -z "$1" ]; then
  echo "Usage: $0 /path/to/RobloxInstaller.exe"
  exit 1
fi

wine "$1"
