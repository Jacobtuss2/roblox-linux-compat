#!/usr/bin/env bash
set -e

echo "Installing Raspberry Pi 5 compatibility dependencies..."

sudo apt update
sudo apt install -y \
  wget curl git build-essential python3 python3-pip \
  mesa-vulkan-drivers vulkan-tools \
  wine64 winetricks \
  python3-pyqt5 \
  xorg xserver-xorg-core \
  libsdl2-2.0-0 libvulkan1 \
  dosbox \
  p7zip-full \
  unzip \
  jq

echo "Optional compatibility tools:"

echo "- Box64 / Box86 may be added if your specific runtime requires x86_64 compatibility support."
echo "- DXVK and VKD3D are normally installed via winetricks or the helper install script."

echo "Dependencies installed."
