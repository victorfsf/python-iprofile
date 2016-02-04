clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;

requirements:
	@pip install -r requirements.txt

test:
	@py.test --cov=pythinkdb tests/
	@coverage html

test.warn:
	@py.test --cov=pythinkdb tests/ -rw
	@coverage html

setup: clean requirements test
