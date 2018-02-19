PYTHONEXE=python -B
TEST_ENV = local
# DO NOT rename it to PYTHONPATH as it will lead to weird issues!
PYTHON_INCLUDEPATH=../src/:$(PYTHONPATH)
PYTESTARGS=
# Once there will be more tests we might enable parallelism
#PYTESTARGS=-n 4

PYTHONTESTS=--ignore ./python/fixtures/ python/

all: test

test: unit

unit: python


python:
	TEST_FIXTURES=$(shell pwd)/python/fixtures TEST_ENV=$(TEST_ENV) PYTHONPATH=$(PYTHON_INCLUDEPATH) $(PYTHONEXE) -mpytest --doctest-modules $(PYTESTARGS) $(PYTHONTESTS) 

.PHONY: all unit python
