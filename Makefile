poetry.install:
	poetry install

poetry.config.native:
	poetry config virtualenvs.create false

poetry.config.venv:
	poetry config virtualenvs.create true
	poetry config virtualenvs.in-project true
	poetry config virtualenvs.path .

fmt:
	black .
	make fmt.check

fmt.check:
	black --check .
	flake8
