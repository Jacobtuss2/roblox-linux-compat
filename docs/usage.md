# Roblox Linux Compatibility Project

This project is intentionally built around a Raspberry Pi 5 compatibility flow using Wine under Linux.

## Project goal

The goal is to provide a lightweight launcher and compatibility runtime for Roblox on Linux, with a focus on the Raspberry Pi 5 and Vulkan-capable setups.

## Typical workflow

1. Install the Linux dependencies:
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

4. Validate the project state:
   ```bash
   PYTHONPATH=src python3 -m launcher.cli status --prefix "$HOME/.roblox-linux-compat"
   ```

5. Launch Roblox:
   ```bash
   PYTHONPATH=src python3 -m launcher.cli launch --prefix "$HOME/.roblox-linux-compat"
   ```

6. Diagnose failures if needed:
   ```bash
   PYTHONPATH=src python3 -m launcher.cli diagnose --prefix "$HOME/.roblox-linux-compat"
   ```

## Command-line entry points

```bash
python3 launcher.py status
python3 launcher.py launch
python3 launcher.py diagnose
```

## Notes

- The repository is intentionally compatibility-focused, not a native Linux Roblox client.
- Environment variables and Wine prefix paths are centralized in the launcher configuration.
- This project is best treated as a compatibility engineering project for Linux-based Raspberry Pi hardware.
