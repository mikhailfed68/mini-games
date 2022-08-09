install:
	poetry install

lint:
	poetry run flake8

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=mini_games

selfcheck:
	poetry check

check: selfcheck lint test

build: check
	poetry build

publish: check
	poetry config repositories.testpypi https://test.pypi.org/legacy/
	poetry publish -r testpypi --build

.PHONY: install lint test test-cov selfcheck check build publish