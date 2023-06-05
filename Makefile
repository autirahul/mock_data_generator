MYPY_OPTIONS = --ignore-missing-imports --disallow-untyped-calls --disallow-untyped-defs --disallow-incomplete-defs

.PHONY: install
install:
	pre-commit install || pip install pre-commit
	poetry install

.PHONY: build
build:
	poetry build

.PHONY: test
test:
	poetry run pytest

.PHONY: requirements
requirements:
	poetry export -f requirements.txt --output requirements.txt --dev
