install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

.PHONY: install lint test
