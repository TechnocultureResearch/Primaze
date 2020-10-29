all:
	python ./sandbox.py

test:
	pytest

start:
	pip install -r requirements.txt

init:
	sudo apt-get update
	pip install -r requirements.txt

debug:
	pdb sandbox.py

install:
	python setup.py install

pypi:
	python setup.py sdist bdist_wheel
	twine upload --repository testpypi dist/*
	# https://packaging.python.org/tutorials/packaging-projects/

clean:
	-rm --force --recursive build/ dist/ htmlcov/ .pytest_cache/
	-rm --force --recursive Primaze.egg-info .coverage

.PHONY:
	init test clean
