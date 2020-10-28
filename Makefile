all:
	python ./main.py

init:
	sudo apt-get update
	pip install -r requirements.txt

clean:
	rm --force --recursive build/ dist/ htmlcov/ .pytest_cache/
	rm --force --recursive Primaze.egg-info .coverage

test:
	pytest

install:
	python setup.py install

.PHONY:
	init test clean
