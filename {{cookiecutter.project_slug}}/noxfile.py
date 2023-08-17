import pathlib
import tempfile
import typing

import nox


class RepoCache:
    """class for caching checkouts of downstream repos

    By caching the checkouts for downstream test runs,
    the nox invokation is faster and there is less load
    on the git server and network.
    """

    _checkouts: typing.ClassVar = {}

    @classmethod
    def clone(cls, session: nox.Session, repo: str) -> str:
        """clones a git repo only once

        Arguments:
            session: the nox session in use
            repo: a git repo url

        Returns:
            path to a temporary directory containing the
            cloned git repo
        """
        tmpdir = cls._checkouts.get(repo, None)

        if tmpdir is None:
            tmpdir = tempfile.TemporaryDirectory()
            session.run("git", "clone", repo, tmpdir.name, external=True)
            cls._checkouts[repo] = tmpdir

        return tmpdir.name


@nox.session(python=["3.9", "3.10", "3.11"])
def tests(session):
    session.install(".[test]")

    session.run("pytest", *session.posargs)


@nox.session(python=["3.9", "3.10", "3.11"])
@nox.parametrize(
    "repo",
    [
        "https://git.example.com/user/repo",
    ],
)
def downstream(session, repo):
    tmpdir = RepoCache.clone(session, repo)

    session.install(".")
    session.install(f"{tmpdir}[test]")

    test_path = pathlib.Path(tmpdir) / "tests"
    session.run("pytest", test_path)
