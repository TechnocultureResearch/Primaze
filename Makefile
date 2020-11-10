MAIN= ./main.py
SHELL:= /bin/bash
MODULES= Primaze

all: format
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

lint:
	pylint $(MODULES)

format:
	black ./
	

# =================================================================
start:
	source $(PWD)/.bashrc
	source $(PWD)/venv/bin/activate

init: start
	sudo apt install python3-pip
	pip install -U -r requirements.txt
	# sudo apt-get update

install:
	python setup.py install

pypi:
	python setup.py sdist bdist_wheel
	twine upload --repository testpypi dist/*
	# https://packaging.python.org/tutorials/packaging-projects/

.PHONY:
	init test clean
