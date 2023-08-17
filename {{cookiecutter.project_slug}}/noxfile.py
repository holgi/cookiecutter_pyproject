import pathlib
import tempfile

import nox


@nox.session(python=["3.9", "3.10", "3.11"])
def tests(session):
    session.install(".[test]")

    session.run("pytest", *session.posargs)


@nox.session(python=["3.9", "3.10", "3.11"])
@nox.parametrize(
    ("repo", "test_dir"),
    [
        ("https://git.example.com/user/repo", "tests"),
    ],
)
def downstream(session, repo, test_dir):
    session.install(".")

    with tempfile.TemporaryDirectory() as tmpdir:
        session.run("git", "clone", repo, tmpdir, external=True)

        session.install(f"{tmpdir}[test]")

        test_path = pathlib.Path(tmpdir) / test_dir
        session.run("pytest", test_path)
