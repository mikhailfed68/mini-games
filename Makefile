install:
	poetry install

lint:
	poetry run flake8

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=mini-games

selfcheck:
	poetry check

check: selfcheck lint test

build: check
	poetry build

.PHONY: install lint test test-cov selfcheck check build