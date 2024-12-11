.PHONY: clean clean-build clean-docs clean-pyc clean-test coverage coverall devenv docs help install lint nox repo serve-docs test testall testfunctional tox
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-docs clean-pyc clean-test  ## remove all build, test, coverage and Python artifacts

clean-build:  ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-docs:  ## remove documentation artifacts
	rm -fr site/

clean-pyc:  ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:  ## remove test and coverage artifacts
	rm -fr .mypy_cache/
	rm -fr .pytest_cache/
	rm -fr .ruff_cache/
	rm -fr .nox/
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint:  ## reformat with black and check style with flake8
	uv run ruff format src tests noxfile.py
	uv run ruff check src tests noxfile.py

test: lint  ## run tests quickly, stop on first error
	uv run pytest tests --stepwise --disable-warnings -m "not integration"

testfunctional: lint ## run functional tests, stop on first error
	uv run pytest tests --stepwise -m "integration"

testall: lint  ## run all tests
	uv run pytest tests

coverage: lint  ## functional test suite, check code coverage and open coverage report
	uv run pytest tests --cov={{cookiecutter.project_slug}} -m "integration"
	uv run coverage html
	$(BROWSER) htmlcov/index.html

coverall: lint   ## full test suite, check code coverage and open coverage report
	uv run pytest tests --cov={{cookiecutter.project_slug}} --cov=tests
	uv run coverage html
	$(BROWSER) htmlcov/index.html

nox:  ## run fully isolated tests with nox
	uv run nox

tox:  ## old habits die hard: typo-squatting to use nox
	uv run nox

docs:  ## build the documentation using mkdocs
	uv run mkdocs build

serve-docs: docs  ## build the documentation and serve them in a web server
	uv run mkdocs serve

install:  ## install updated project.toml
	rm -fr .venv/
	uv sync --all-groups

devenv: install  ## setup development environment including precommit hooks
	uv run pre-commit install --install-hooks

repo: install  ## complete project setup with development environment and git repo
	git init .
	git add .
	git commit -m "import of project template"
	git branch -m {{cookiecutter.default_branch}}
	{% if cookiecutter.remote_git_repo != "" -%}
	git remote add origin {{ cookiecutter.remote_git_repo }}
	git push -u origin main --no-verify
	{% endif %}
	uv run pre-commit install --install-hooks
