# roblox-linux-compat

A Linux compatibility project to run Roblox on Raspberry Pi 5 using a Wine/Proton-based runtime and launcher layer.

## Goal
This project aims to provide a Linux-native launcher and compatibility runtime for Roblox on Raspberry Pi 5, using Windows compatibility layers where no native Linux client exists.

## Important note
This is not a native Roblox Linux port. It is a compatibility engineering project designed to run the Roblox client under a Linux-based launcher environment.

## Project structure

- `README.md` — project overview
- `install/`
  - `install_pi5_dependencies.sh` — system dependencies
  - `install_wine_stack.sh` — Wine/DXVK/VKD3D setup
- `src/`
  - `launcher/`
    - `app.py` — launcher entry point
    - `config.py` — configuration management
    - `ui.py` — optional Qt UI
  - `runtime/`
    - `runner.py` — Roblox runner logic
    - `wine_prefix.py` — prefix management
    - `diagnostics.py` — logs and runtime diagnostics
  - `input/`
    - `controllers.py` — controller mapping
    - `mapping.py` — keyboard/mouse mapping
  - `scripts/`
    - `start_roblox.sh` — starts Roblox in the compatibility runtime
    - `debug_roblox.sh` — collects logs and runtime failure data
- `docs/`
  - `setup.md` — setup guide
  - `troubleshooting.md` — common issues
  - `compatibility.md` — compatibility notes

## Hardware target
- Raspberry Pi 5
- Raspberry Pi OS 64-bit (recommended)
- Vulkan-compatible GPU stack

## Compatibility stack
- Wine / Proton-style runtime
- DXVK (DirectX to Vulkan)
- VKD3D (D3D to Vulkan)
- Box64 / Box86 if needed for x86_64 compatibility
- Linux launcher UI and input remapping

## First-pass install flow
```bash
chmod +x install/install_pi5_dependencies.sh
./install/install_pi5_dependencies.sh
./install/install_wine_stack.sh
```

## Planned milestones
1. Create a clean Wine prefix
2. Install Roblox launcher inside the prefix
3. Launch Roblox and capture failures
4. Fix missing DLLs and runtime dependencies
5. Add graphics compatibility layer tuning
6. Add input remapping and controller support
7. Create launcher UI
8. Stabilize startup and runtime behavior

## Repository status
This repository is the initial scaffold for the Linux compatibility project.
