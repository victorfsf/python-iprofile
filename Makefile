clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name '__pycache__' -exec rm -fr {} \;

requirements:
	@pip install -r requirements.txt

coverage:
	@coverage run --source=iprofile -m tests.__init__

test:
	@py.test --cov-config .coveragerc --cov=iprofile tests/

test.html: test
	@coverage html

test.warn:
	@py.test --cov-config .coveragerc --cov=iprofile tests/ -rw

setup: clean requirements test

cov.badge:
	@rm -rf coverage.svg
	@coverage-badge -o coverage.svg
