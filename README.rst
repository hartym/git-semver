git-semver
==========

Install
:::::::

    pip install git-semver

Usage
:::::

    $ git semver -h
    usage: git-semver [-h] [--next-patch] [--next-minor] [--next-major]

    optional arguments:
      -h, --help        show this help message and exit
      --next-patch, -p
      --next-minor, -m
      --next-major, -M

    $ git semver
    0.1.0

    $ git semver --next-patch
    0.1.1

    $ git semver --next-minor
    0.2.0

    $ git semver --next-major
    1.0.0
