install:
	poetry install

build:
	poetry build

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

package-install:
	python3 -m pip install dist/*.whl

 publish:
	poetry publish --dry-run

make lint:
	poetry run flake8 brain_games



.PHONY: install test lint selfcheck check build



