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
	@py.test --cov=iprofile tests/

test.warn:
	@py.test --cov=iprofile tests/ -rw
	@coverage html

setup: clean requirements test

cov.badge:
	@rm -rf coverage.svg
	@coverage-badge -o coverage.svg
