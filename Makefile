MAIN= ./Sandbox.py
SHELL:= /bin/bash

all:
	python $(MAIN)

test:
	pytest

debug:
	pdb $(MAIN)

clean:
	-rm --force --recursive build/ log/ dist/ htmlcov/ .pytest_cache/
	-rm --force --recursive Primaze.egg-info .coverage

# ...
start:
	-source $(PWD)/.bashrc
	-source $(PWD)/venv/bin/activate

init:
	sudo apt-get update
	start
	pip install -r requirements.txt

install:
	python setup.py install

pypi:
	python setup.py sdist bdist_wheel
	twine upload --repository testpypi dist/*
	# https://packaging.python.org/tutorials/packaging-projects/

.PHONY:
	init test clean
