#!/usr/bin/env bash
set -e

export WINEDLLOVERRIDES="winemenubuilder.exe=d"
export WINEPREFIX="$HOME/.roblox-linux-compat"
mkdir -p "$WINEPREFIX"

wineboot --init
winetricks corefonts vcrun2022 dxvk vkd3d

cat <<'EOF'
Wine compatibility runtime is ready.

Next steps:
- install the Roblox launcher within the Wine prefix
- test Roblox startup under Wine
- capture logs and fix runtime failures
EOF
