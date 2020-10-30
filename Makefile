MAIN= ./main.py
SHELL:= /bin/bash
MODULES= Pricore Primaze

all: #type
	python $(MAIN)

test:
	pytest

debug:
	pdb $(MAIN)

clean:
	-rm --force --recursive build/ log/*.log dist/ htmlcov/ .pytest_cache/
	-rm --force --recursive Primaze.egg-info .coverage

type:
	mypy $(MODULES) $(MAIN)

lint: #type
	pylint $(MODULES)


# =================================================================
start:
	-source $(PWD)/.bashrc
	-source $(PWD)/venv/bin/activate

init: start
	# sudo apt-get update
	pip install -r requirements.txt

install:
	python setup.py install

pypi:
	python setup.py sdist bdist_wheel
	twine upload --repository testpypi dist/*
	# https://packaging.python.org/tutorials/packaging-projects/

.PHONY:
	init test clean
