all:
	python ./main.py

init:
	sudo apt-get update
	pip install -r requirements.txt

test:
	pytest

.PHONY:
	init test