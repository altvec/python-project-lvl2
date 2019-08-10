all: install

install: build
	@pip install --user dist/altvec_gendiff-*.whl

configure:
	@poetry install

lint:
	@poetry run flake8 gendiff

test:
	@poetry run pytest -v

build: lint test
	@poetry build

.PHONY: all install configure lint test build
