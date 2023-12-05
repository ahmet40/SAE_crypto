MODULES=code/SDES.py code/SDES_base.py
TEST = tests/*.py

.PHONY: typehint
typehint:  
	mypy --ignore-missing-imports ${MODULES}

.PHONY: tests
tests:  
	python -m unittest -v -b ${TEST}
.PHONY: lint
lint:  
	pylint ${MODULES}

.PHONY: format
format:	
	yapf -ir ${MODULES}

.PHONY: coverage
coverage:
	python -m coverage run -m unittest
	python -m coverage report

.PHONY: checklist
checklist: lint typehint tests

.PHONY: clean
clean:  
	find . -type f -name "*.pyc" | xargs rm -fr  
	find . -type d -name __pycache__ | xargs rm -fr