install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=mylib --cov=app test_app.py

lint:
	pylint --disable=R,C app.py mylib/*.py

format:
	black *.py mylib/*.py

all: install test lint