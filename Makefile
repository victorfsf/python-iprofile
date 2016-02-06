clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;

requirements:
	@pip install -r requirements.txt

test:
	@py.test --cov=iprofile tests/
	@coverage html

test.warn:
	@py.test --cov=iprofile tests/ -rw
	@coverage html

setup: clean requirements test

cov.badge:
	@rm -rf coverage.svg
	@coverage-badge -o coverage.svg
