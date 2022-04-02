install:
	poetry install

build:
	poetry build

brain-games:
	poetry run brain-games

package-install:
	python3 -m pip install --user dist/*.whl

publish:
	poetry publish --dry-run



.PHONY: install test lint selfcheck check build



