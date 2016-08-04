git-semver
==========

Install
:::::::

.. code-block:: shell

    (sudo) pip install git-semver

Usage
:::::

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
    
Simple release process using git-semver
:::::::::::::::::::::::::::::::::::::::

.. code-block:: shell

    git semver -p > version.txt
    git add version.txt
    git commit -m 'Release: '`cat version.txt`
    git tag -am `cat version.txt` `cat version.txt`
    git push origin --tags
