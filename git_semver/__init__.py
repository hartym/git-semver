from semantic_version import Version as _Version


def get_current_version(repo, Version=_Version):
    latest = None
    for tag in repo.tags:
        v = tag.name
        if v.startswith('v.'):
            v = v[2:]
        elif v.startswith('v'):
            v = v[1:]

        v = Version.coerce(v, partial=True)

        if not latest:
            latest = v
        else:
            if v > latest:
                latest = v

    return latest
