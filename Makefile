.PHONY: install-dev test lint format build

install-dev:
	python -m pip install -e ".[dev]"

test:
	pytest -q

lint:
	ruff check .

format:
	ruff format .

build:
	python -m build
