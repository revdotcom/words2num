PROJECT=words2num
PYTHON := /usr/bin/env python
PYTHON_VERSION=$(shell $(PYTHON) -c 'from __future__ import print_function; import sys; print(sys.version_info[0])')
PRJ_VERSION=$(shell $(PYTHON) -c 'from __future__ import print_function; import words2num; print(words2num.__version__)')

default:
	@echo "install: install the package and scripts"
	@echo "clean: remove build/test artifacts"
	@echo "lint: check syntax"
	@echo "test: run unit tests"
	@echo 
	@echo "Python Version: $(PYTHON_VERSION)"
	@echo "Module Version: $(PRJ_VERSION)"

install:
	python setup.py install

clean:
	find . -name \*.pyc -exec rm -f {} \;
	find . -depth -type d -name __pycache__ -exec rm -rf {} \;
	rm -rf build dist $(PROJECT).egg-info

lint:
	@echo Checking for Python syntax...
	flake8 --ignore=E123,E501 $(PROJECT) && echo OK

test:
	@echo Running tests...
	nosetests --with-coverage --cover-package=$(PROJECT)

wheel: dist/words2num-$(PRJ_VERSION)-py$(PYTHON_VERSION)-none-any.whl

sdist: dist/words2num-$(PRJ_VERSION).tar.gz

dist/words2num-$(PRJ_VERSION)-py$(PYTHON_VERSION)-none-any.whl:
	$(PYTHON) setup.py bdist_wheel

dist/words2num-$(PRJ_VERSION).tar.gz:
	$(PYTHON) setup.py sdist
