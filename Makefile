.PHONY: install-deps setup-wine install-roblox status launch diagnose help

PYTHON ?= python3
APP = launcher.py
SRC = src

help:
	@echo "Available targets:"
	@echo "  install-deps    install Python dependencies"
	@echo "  setup-wine      initialize the Wine prefix"
	@echo "  install-roblox  install Roblox from an installer file"
	@echo "  status          validate the Wine prefix and Roblox launcher"
	@echo "  launch          start Roblox through the compatibility stack"
	@echo "  diagnose        collect runtime diagnostics"

install-deps:
	$(PYTHON) -m pip install -r requirements.txt

setup-wine:
	bash ./install/install_wine_stack.sh

install-roblox:
	@if [ -z "$(ROBLOX_INSTALLER)" ]; then \
		echo "Usage: make install-roblox ROBLOX_INSTALLER=/path/to/RobloxInstaller.exe"; \
		exit 1; \
	fi
	bash ./src/scripts/install_roblox.sh "$(ROBLOX_INSTALLER)"

status:
	PYTHONPATH=$(SRC) $(PYTHON) -m launcher.cli status --prefix "$${WINEPREFIX:-$$HOME/.roblox-linux-compat}"

launch:
	PYTHONPATH=$(SRC) $(PYTHON) -m launcher.cli launch --prefix "$${WINEPREFIX:-$$HOME/.roblox-linux-compat}"

diagnose:
	PYTHONPATH=$(SRC) $(PYTHON) -m launcher.cli diagnose --prefix "$${WINEPREFIX:-$$HOME/.roblox-linux-compat}"
