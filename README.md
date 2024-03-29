Cookiecutter PyProject
======================

**Cookiecutter template for a Python project.**

This is heavily inspired the [cookiecutter-pypackage][coopy] by Audrey Roy Greenfeld.


Features
--------

- [flit][flit]: build and packaging tool
- [pytest][pytest]: for running tests, including coverage
- [nox][nox] testing: for running extended isolated tests
- [black][black]: the uncompromising code formatter
- [ruff][ruff]: python linting
- [precommit][preco]: a selection of preinstalled pre-commit hooks


Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/holgi/cookiecutter_pyproject.git

Then change to the project and setup the repo and development environment:

    cd <your project dir>
    make repo
    source .venv/bin/activate


Make commands in the new project
--------------------------------

The new project contains a Makefile defining different commands to ease the
developers work:

- `clean`: combines the following all `clean-*` commands into one
- `clean-build`: remove build artifacts
- `clean-pyc`: remove Python file artifacts
- `clean-test`: remove test and coverage artifacts

- `lint`: reformat with black and check style with flake8
- `test`: run unit tests quickly, without the ones marked as `functional`, will stop on first error
- `testfunctional`: run only tests marked as `functional`
- `testall`: run the complete test suite
- `coverage`: runs tests marked as `functional`only, check code coverage and open report
- `coverall`: runs all tests, check code coverage and open report
- `tox`: run fully isolated tests with tox

- `install`: install updated project.toml with flint

- `devenv`: setup development environment

- `repo`: complete project setup with development environment and git repo




[coopy]: https://github.com/audreyr/cookiecutter-pypackage/
[flit]: https://flit.readthedocs.io/
[pytest]: https://docs.pytest.org/
[nox]: https://nox.thea.codes
[black]: https://black.readthedocs.io/
[ruff]: https://github.com/charliermarsh/ruff
[preco]: https://pre-commit.com
