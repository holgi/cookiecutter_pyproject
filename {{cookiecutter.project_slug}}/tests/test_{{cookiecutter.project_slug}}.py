""" Stub file for testing the project

There are three predefined ways to run tests:

make test:
    runs only unit tests, that are not marked with "fun" (for functional test)
    in a random order. If a test failed before, only the failed tests will be
    run. This is intended to be the default testing method while developing.

make testall:
    runs unit tests and functional tests in random order. Will give a complete
    overview of the test suite.

make coverage:
    runs only tests marked with "fun" (for functional tests) and generates a
    coverage report for the test run. The idea is to check the test coverage
    only on functinal tests to see if a) everything is as much covered as
    possible and b) to find dead code that is not called in end-to-end tests.

all three test strategies will run "make lint" before to catch easily made
mistakes.
"""

import pytest


def test_example_unittest():
    """example unittest - try importing the project

    will be run by 'make test' and 'make testall' but not 'make  coverage'
    """
    import {{ cookiecutter.project_slug }}  # noqa: F401

    assert True


@pytest.mark.integration()
def test_example_integration_test():
    """example unittest

    will be by 'make  coverage' and 'make testall' but not 'make test'
    """
    import {{ cookiecutter.project_slug }}  # noqa: F401

    assert True
