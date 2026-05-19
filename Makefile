.PHONY: install run debug clean lint lint-strict repackage

UV := $(shell command -v uv 2>/dev/null)
PYTHON := .venv/bin/python
PIP := .venv/bin/pip

MODULE ?= 0
EXERCISE ?= 0

ARGS := main.py

install:
	@if [ -z "$(UV)" ]; then \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
		export PATH=$$PATH:$$HOME/.local/bin/uv; \
		UV=$$(command -v uv 2>/dev/null); \
	fi
	@if [ ! -d ".venv" ]; then \
		uv venv; \
	fi
	@$(PYTHON) -m ensurepip --upgrade || \
		curl -s https://bootstrap.pypa.io/get-pip.py | $(PYTHON)
	$(PYTHON) -m pip install --upgrade pip setuptools wheel build \
		flake8 pydantic pyperclip tqdm numpy Pillow matplotlib pyclustering scipy scikit-learn

textures:
	git clone -b 26.1.2 https://github.com/PixiGeko/Minecraft-default-assets
	@if [ ! -d .venv ]; then \
		echo "Run make install first"; \
		exit 1; \
	fi
	$(PYTHON) main.py


run:
	@if [ ! -d .venv ]; then \
		echo "Run make install first"; \
		exit 1; \
	fi
	$(PYTHON) $(ARGS)

debug:
	$(PYTHON) -m pdb $(ARGS)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -name ".pytest_cache" -exec rm -rf {} +
	find . -name "*.pyc" -delete
	find . -name "*.pyo" -delete
	cd $(PCKG) && rm -rf dist build *.egg-info

lint:
	$(PYTHON) -m flake8 $(ARGS)

lint-strict:
	$(PYTHON) -m flake8 $(ARGS) --max-line-length=100

repackage:
	cd $(PCKG) && rm -rf dist build *.egg-info
	$(PYTHON) -m pip install --upgrade build setuptools wheel
	$(PYTHON) -m build $(PCKG)
	$(PIP) install --force-reinstall $(PCKG)/dist/\
											ft_package-0.0.1-py3-none-any.whl
