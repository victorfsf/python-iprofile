clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name '__pycache__' -exec rm -fr {} \;

requirements:
	@pip install -r requirements.txt

pytest:
	@py.test tests/

coverage:
	@py.test --cov-config .coveragerc --cov-report html --cov=iprofile tests/

test.warn:
	@py.test --cov-config .coveragerc --cov-report html --cov=iprofile tests/ -rw

setup: clean requirements test

cov.badge:
	@rm -rf coverage.svg
	@coverage-badge -o coverage.svg
