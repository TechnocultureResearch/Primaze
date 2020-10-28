init:
	sudo apt-get update && sudo apt-get upgrade
	pip install -r requirements.txt

test:
	# python tests/context.py
	pytest

.PHONY:
	init test