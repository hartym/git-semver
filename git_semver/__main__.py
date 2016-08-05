#! /usr/bin/env python

from __future__ import absolute_import, print_function, unicode_literals

import argparse
import os
import sys

from git import Repo
from semantic_version import Version

ERR_NO_VERSION_FOUND = 1
ERR_NOT_A_REPO = 128


def get_current_version(repo):
    latest = None
    for tag in repo.tags:
        v = tag.name
        if v.startswith('v.'):
            v = v[2:]
        elif v.startswith('v'):
            v = v[1:]

        v = Version.coerce(v)

        if not latest:
            latest = v
        else:
            if v > latest:
                latest = v

    return latest


def main(args=None):
    parser = argparse.ArgumentParser()

    parser.add_argument('--next-patch', '-p', dest='modifier', action='store_const', const=Version.next_patch)
    parser.add_argument('--next-minor', '-m', dest='modifier', action='store_const', const=Version.next_minor)
    parser.add_argument('--next-major', '-M', dest='modifier', action='store_const', const=Version.next_major)

    options = parser.parse_args(sys.argv[1:] if args is None else args)

    try:
        repo = Repo(os.path.join(os.getcwd()))
    except:
        print('fatal: Not a git repository', file=sys.stderr)
        return ERR_NOT_A_REPO

    version = get_current_version(repo)
    if version is None:
        print('No version found. Try creating a tag with your initial version, for example:', file=sys.stderr)
        print('  git tag -am 0.1.0 0.1.0', file=sys.stderr)
        return ERR_NO_VERSION_FOUND

    if options.modifier:
        version = options.modifier(version)

    print(version)
    return 0
