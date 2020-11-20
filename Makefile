all: install

install:
	@poetry install

package-install:
	@pip install --user --index-url https://test.pypi.org/simple/ \
	    --extra-index-url https://pypi.org/simple/ altvec-gendiff

lint:
	@poetry run flake8 gendiff

test:
	poetry run coverage run --source=gendiff -m pytest tests

cc-coverage:
	poetry run coverage xml

build: lint test
	@poetry build

.PHONY: all install package-install configure lint test build
