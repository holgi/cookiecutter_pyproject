.PHONY: clean coverage coverall docs devenv install lint prepareenv repo test testall testfunctional tox
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

clean: clean-build clean-docs clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-docs: ## remove documentation artifacts
	rm -fr site/

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
	black src tests
	ruff src tests

test: lint ## run tests quickly, stop on first error
	pytest tests -x -l --last-failed --disable-warnings -m "not functional"

testfunctional: lint ## run functional tests, stop on first error
	pytest tests -x -l -m "functional"

testall: lint ## run all tests
	pytest tests -l

coverage: lint ## functional test suite, check code coverage and open coverage report
	pytest tests --cov={{cookiecutter.project_slug}} -l -m "functional"
	coverage html
	$(BROWSER) htmlcov/index.html

coverall: lint ## full test suite, check code coverage and open coverage report
	pytest tests --cov={{cookiecutter.project_slug}} -l
	coverage html
	$(BROWSER) htmlcov/index.html

tox:  ## run fully isolated tests with tox
	tox

docs:  ## build the documentation using mkdocs
	mkdocs build

serve-docs: docs  ## build the documentation and serve them in a web server
	mkdocs serve

install:  ## install updated project.toml
	.venv/bin/pip3 install -e ".[docs,dev,test]"

prepareenv: ## helper to create virtual environment and install basic packages
	rm -fr .venv/
	python3 -m venv --prompt {{cookiecutter.project_slug}} .venv
	.venv/bin/pip3 install --upgrade pip
	.venv/bin/pip3 install wheel
	.venv/bin/pip3 install -e ".[docs,dev,test]"

devenv: prepareenv ## setup development environment including precommit hooks
	.venv/bin/pre-commit install --install-hooks

repo: prepareenv ## complete project setup with development environment and git repo
	git init .
	git add .
	git commit -m "import of project template"
	git branch -m {{cookiecutter.default_branch}}
	{% if cookiecutter.remote_git_repo != "" -%}
	git remote add origin {{ cookiecutter.remote_git_repo }}
	git push -u origin main --no-verify
	{% endif %}
	.venv/bin/pre-commit install --install-hooks
