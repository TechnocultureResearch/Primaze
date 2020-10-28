all:
	python ./main.py

init:
	sudo apt-get update
	pip install -r requirements.txt

lint:
	# ...

install:
	python setup.py install

# pypi:
# 	python setup.py register

clean:
	-rm -rf build dist Primaze.egg-info

test:
	pytest

.PHONY:
	init test clean