# Setup guide

## 1. Prepare the Raspberry Pi 5

Use a 64-bit Raspberry Pi OS environment. Then install the base Linux dependencies:

```bash
chmod +x install/install_pi5_dependencies.sh
./install/install_pi5_dependencies.sh
```

## 2. Initialize the compatibility stack

```bash
chmod +x install/install_wine_stack.sh
./install/install_wine_stack.sh
```

This configures a Wine prefix at:

```bash
$HOME/.roblox-linux-compat
```

## 3. Install Roblox inside the Wine prefix

You need a Roblox installer file or launcher package that can run under Wine.

```bash
chmod +x src/scripts/install_roblox.sh
./src/scripts/install_roblox.sh /path/to/RobloxInstaller.exe
```

## 4. Start Roblox

```bash
chmod +x src/scripts/start_roblox.sh
./src/scripts/start_roblox.sh
```

## 5. Debug failures

```bash
chmod +x src/scripts/debug_roblox.sh
./src/scripts/debug_roblox.sh
```

## Notes

- Some Roblox features may not function correctly under compatibility layers.
- Pi 5 performance can limit gameplay quality.
- This project is best treated as a compatibility engineering effort rather than a supported Linux native client.
