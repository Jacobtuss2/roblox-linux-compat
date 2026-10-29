# Troubleshooting

## Roblox does not start

Check the following:

- Wine prefix exists at `$HOME/.roblox-linux-compat`
- Roblox launcher actually exists in the prefix
- Required DLLs and fonts were installed with `winetricks`
- Vulkan support is available on the Pi 5

## Graphics issues

Try checking the environment variables:

```bash
export DXVK_ASYNC=1
export VKD3D_CONFIG="dxr,dxr11"
```

If issues persist, verify that `vulkan-tools` and the Mesa Vulkan drivers are installed.

## Input issues

Use the input mapping scripts under `src/input` to configure keyboard, mouse, and controller mappings.

## Log collection

Use:

```bash
./src/scripts/debug_roblox.sh
```

This will dump runtime and launch diagnostics to the console and log file.

## Common caveats

- Some Roblox games may fail due to runtime incompatibility.
- Performance may be limited on Raspberry Pi 5 hardware.
- This project targets compatibility rather than official Linux support.
