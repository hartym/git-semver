from semantic_version import Version as _Version

from git_semver._version import __version__


def get_current_version(repo, Version=_Version):
    latest = None
    for tag in repo.tags:
        v = tag.name
        if v.startswith("v."):
            v = v[2:]
        elif v.startswith("v"):
            v = v[1:]

        try:
            v = Version(v)
        except ValueError:
            # Could not parse ...
            # Maybe a prerelease which is not supported anymore by latest semantic_version package.
            continue

        if not latest or v > latest:
            latest = v

    return latest
