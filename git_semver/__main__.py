#! /usr/bin/env python

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
    repo = Repo(os.path.join(os.getcwd()))
    version = get_current_version(repo)

    if options.modifier:
        version = options.modifier(version)

    print(version)
