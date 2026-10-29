# Roblox Linux Compatibility Project

This project is intended to provide a Linux-native launcher and compatibility runtime for Roblox on Raspberry Pi 5.

## Overview

Roblox does not officially support Linux, so this project targets a compatibility path using a Windows runtime under Linux. The project includes:

- Linux launcher UI
- Wine/DXVK/VKD3D compatibility runtime setup
- Roblox launcher path and startup wrappers
- debug and runtime diagnostics
- controller and input mapping tools

## Target platform

- Raspberry Pi 5
- Raspberry Pi OS 64-bit
- Vulkan-capable graphics stack

## Compatibility model

This is a Linux compatibility project, not a native Roblox Linux client. The goal is to launch Roblox through a Windows-compatible runtime environment under Linux.

## Quick start

1. Install dependencies:
   ```bash
   ./install/install_pi5_dependencies.sh
   ```

2. Initialize the Wine runtime stack:
   ```bash
   ./install/install_wine_stack.sh
   ```

3. Install Roblox inside the Wine prefix:
   ```bash
   ./src/scripts/install_roblox.sh /path/to/RobloxInstaller.exe
   ```

4. Validate the runtime state:
   ```bash
   PYTHONPATH=src python3 -m launcher.cli status
   ```

5. Launch Roblox:
   ```bash
   ./src/scripts/start_roblox.sh
   ```

6. Run diagnostics if startup fails:
   ```bash
   PYTHONPATH=src python3 -m launcher.cli diagnose
   ```

## Repository layout

- `install/` — Linux system and Wine compatibility installation scripts
- `src/launcher/` — launcher logic, config, and CLI
- `src/runtime/` — compatibility runtime and debug helpers
- `src/input/` — input mapping for keyboard, mouse, controller
- `src/scripts/` — startup and install wrappers
- `docs/` — setup and troubleshooting guides

## Command-line workflow

```bash
PYTHONPATH=src python3 -m launcher.cli status
PYTHONPATH=src python3 -m launcher.cli launch
PYTHONPATH=src python3 -m launcher.cli diagnose
```
