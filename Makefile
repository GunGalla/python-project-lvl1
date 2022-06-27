install: 
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl 
	python3 -m pip install --user --force-reinstall dist/*.whl

start: 
	poetry run brain-games

.PHONY: install
