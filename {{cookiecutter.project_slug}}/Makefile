.PHONY: clean clean-test clean-pyc clean-build docs help
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

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .pytest_cache/
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

lint: ## reformat with black and check style with flake8
	isort -rc {{cookiecutter.project_slug}}
	isort -rc tests
	black {{cookiecutter.project_slug}} tests
	flake8 {{cookiecutter.project_slug}} tests

test: lint ## run tests quickly with the default Python
	pytest tests -x --disable-warnings -m "not app"

coverage: lint ## full test suite, check code coverage and open coverage report
	pytest tests --cov={{cookiecutter.project_slug}}
	coverage html
	$(BROWSER) htmlcov/index.html

tox:  ## run fully isolated tests with tox
	tox

install:  ## install updated project.toml with flint
	flit install --pth-file

devenv: ## setup development environment
	python3 -m venv --prompt {{cookiecutter.project_slug}} .venv
	.venv/bin/pip3 install --upgrade pip
	.venv/bin/pip3 install flit
	.venv/bin/flit install --pth-file

repo: devenv ## complete project setup with development environment and git repo
	git init .
	git add .
	git commit -m "import of project template"
	{% if cookiecutter.remote_git_repo != "" -%}
	git remote add origin {{ cookiecutter.remote_git_repo }}
	git push -u origin master --no-verify
	{% endif %}
	.venv/bin/pre-commit install --install-hooks
