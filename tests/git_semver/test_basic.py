from __future__ import absolute_import, print_function, unicode_literals

import os

import pytest

from git_semver.__main__ import ERR_NO_VERSION_FOUND, ERR_NOT_A_REPO
from git_semver.__main__ import main as git_semver


@pytest.yield_fixture()
def tmpdir(tmpdir_factory):
    working_directory = os.getcwd()
    new_working_directory = tmpdir_factory.mktemp("work")
    os.chdir(str(new_working_directory))
    yield new_working_directory
    os.chdir(working_directory)


def test_no_repo(tmpdir, capsys):
    retval = git_semver(())
    assert retval == ERR_NOT_A_REPO
    out, err = capsys.readouterr()
    assert out == ""
    assert err == "fatal: Not a git repository\n"


def test_no_tag(tmpdir, capsys):
    os.system("git init")
    retval = git_semver(())
    assert retval == ERR_NO_VERSION_FOUND
    out, err = capsys.readouterr()
    assert out == ""
    assert err.startswith("No version found.")


def _git_tag_version(version):
    os.system('git commit --allow-empty -m "release: {}"'.format(version))
    os.system("git tag -am {0} {0}".format(version))


def _git_init_create_version(version="3.2.1"):
    os.system("git init")
    os.system('git config user.email "tests@example.com"')
    os.system('git config user.name "Py Test"')
    _git_tag_version(version)


@pytest.mark.parametrize("arg", ["--next-patch", "-p"])
@pytest.mark.parametrize("version", ["v.3.2.1", "v3.2.1", "3.2.1"])
def test_patch(tmpdir, capsys, arg, version):
    _git_init_create_version(version)
    assert git_semver((arg,)) == 0
    out, err = capsys.readouterr()
    assert out == "3.2.2\n"
    assert err == ""


@pytest.mark.parametrize("arg", ["--next-minor", "-m"])
@pytest.mark.parametrize("version", ["v.3.2.1", "v3.2.1", "3.2.1"])
def test_minor(tmpdir, capsys, arg, version):
    _git_init_create_version(version)
    assert git_semver((arg,)) == 0
    out, err = capsys.readouterr()
    assert out == "3.3.0\n"
    assert err == ""


@pytest.mark.parametrize("arg", ["--next-major", "-M"])
@pytest.mark.parametrize("version", ["v.3.2.1", "v3.2.1", "3.2.1"])
def test_major(tmpdir, capsys, arg, version):
    _git_init_create_version(version)
    assert git_semver((arg,)) == 0
    out, err = capsys.readouterr()
    assert out == "4.0.0\n"
    assert err == ""


def test_multiple_tags(tmpdir, capsys):
    _git_init_create_version("0.1.0")
    _git_tag_version("v0.1.1")
    _git_tag_version("v.0.2.0")
    _git_tag_version("v.0.1.7")
    _git_tag_version("0.2.1")
    _git_tag_version("0.1.8")

    # current
    assert git_semver(()) == 0
    assert capsys.readouterr() == ("0.2.1\n", "")
