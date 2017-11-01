Reference
=========

Current version numbers are read from git tags, if you never tagged a commit with a
`semantic version number <http://semver.org/>`_, start by doing so.

git semver
::::::::::

Dumps current version number to stdout.

git semver --next-patch (or -p)
:::::::::::::::::::::::::::::::

Dumps the next version number to use incrementing the patch number.

git semver --next-minor (or -m)
:::::::::::::::::::::::::::::::

Dumps the next version number to use incrementing the minor version.

git semver --next-major (or -M)
:::::::::::::::::::::::::::::::

Dumps the next version number to use incrementing the major version.
