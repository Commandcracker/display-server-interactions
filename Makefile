setup:
	python setup.py bdist_wheel sdist
install:
	pip install -e .
#upload:
#	twine upload dist/*

all: setup install #upload

.PHONY: docs
docs:
	cd docs; make html
