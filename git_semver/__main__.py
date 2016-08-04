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

    subparsers = parser.add_subparsers(dest='version')
    subparsers.required = True

    parser_current = subparsers.add_parser('current', help='Current version')
    parser_current.set_defaults(get_version=get_current_version)

    parser_current = subparsers.add_parser('next', help='Next version (increments patch number)')
    parser_current.set_defaults(get_version=get_next_patch_version)

    parser_current = subparsers.add_parser('next-minor', help='Next minor version')
    parser_current.set_defaults(get_version=get_next_minor_version)

    parser_current = subparsers.add_parser('next-major', help='Next major version')
    parser_current.set_defaults(get_version=get_next_major_version)

    options = parser.parse_args(args or sys.argv[1:])

    repo = Repo(os.path.join(os.getcwd()))

    version = options.get_version(repo)
    print(version)
