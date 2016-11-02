git-semver
==========

.. image:: https://travis-ci.org/hartym/git-semver.svg?branch=master
    :target: https://travis-ci.org/hartym/git-semver
    :alt: Continuous Integration Status

.. image:: https://coveralls.io/repos/github/hartym/git-semver/badge.svg?branch=master
    :target: https://coveralls.io/github/hartym/git-semver?branch=master
    :alt: Coverage Status

.. image:: https://readthedocs.org/projects/git-semver/badge/?version=latest
    :target: http://git-semver.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status


Install
:::::::

.. code-block:: shell

    (sudo) pip install git-semver

Simple usage
::::::::::::

.. code-block:: shell

    $ git semver
    0.1.0

.. code-block:: shell

    $ git semver --next-patch
    0.1.1

.. code-block:: shell

    $ git semver --next-minor
    0.2.0

.. code-block:: shell

    $ git semver --next-major
    1.0.0


Example release process
:::::::::::::::::::::::

See http://rdc.li/release

