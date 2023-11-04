PATH  := $(PATH)
SHELL := /bin/bash

pre-commit:
	poetry run pre-commit run --all-files

test-without-clean:
	set -o pipefail; \
	poetry run pytest \
	  --color=yes \
	  --junitxml=pytest.xml \
	  --cov-report=term-missing:skip-covered \
	  --cov=app \
	  tests \
	  | tee pytest-coverage.txt

test:
	make test-without-clean
	make clean

run:
	poetry run python -m gunicorn -c settings/gunicorn.conf.py app.main:app

run-dev:
	poetry run python -m uvicorn --reload app.main:app

clean:
	rm -f pytest.xml
	rm -f pytest-coverage.txt

