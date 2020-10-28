all:
	python ./sandbox.py

test:
	pytest

init:
	sudo apt-get update
	pip install -r requirements.txt

debug:
	pdb sandbox.py

install:
	python setup.py install

clean:
	rm --force --recursive build/ dist/ htmlcov/ .pytest_cache/
	rm --force --recursive Primaze.egg-info .coverage

.PHONY:
	init test clean
