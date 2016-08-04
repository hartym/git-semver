#! /usr/bin/env python

from __future__ import absolute_import, print_function, unicode_literals

import argparse
import os
import sys

from git import Repo
from semantic_version import Version


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


def get_next_patch_version(repo):
    version = get_current_version(repo)
    return version.next_patch()


def get_next_minor_version(repo):
    version = get_current_version(repo)
    return version.next_minor()


def get_next_major_version(repo):
    version = get_current_version(repo)
    return version.next_major()


def main(args=None):
    parser = argparse.ArgumentParser()

    parser.add_argument('--next-patch', '-p', dest='modifier', action='store_const', const=Version.next_patch)
    parser.add_argument('--next-minor', '-m', dest='modifier', action='store_const', const=Version.next_minor)
    parser.add_argument('--next-major', '-M', dest='modifier', action='store_const', const=Version.next_major)

    options = parser.parse_args(args or sys.argv[1:])

    try:
        repo = Repo(os.path.join(os.getcwd()))
    except:
        print('fatal: Not a git repository (or any of the parent directories)', file=sys.stderr)
        return 128

    version = get_current_version(repo)
    if version is None:
        print('No version found. Try creating a tag with your initial version, for example:')
        print('  git tag -am 0.1.0 0.1.0')
        return 1

    if options.modifier:
        version = options.modifier(version)

    print(version)
    return 0
