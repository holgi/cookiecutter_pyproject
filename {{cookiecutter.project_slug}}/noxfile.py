import nox


@nox.session(python=["3.9", "3.10", "3.11"])
def tests(session):
    session.install(".[test]")

    session.run("pytest", *session.posargs)
