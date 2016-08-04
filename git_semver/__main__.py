#! /usr/bin/env python

import argparse
import os
import sys

from git import Repo
from semantic_version import Version



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', type=str.lower, choices=('all', 'patch', 'minor', 'major'), nargs='?', default='patch')
    options = parser.parse_args(sys.argv[1:])

    repo = Repo(os.path.join(os.getcwd()))

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

    if options.command == 'all':
        print('latest:', latest)
        print('next major:', latest.next_major())
        print('next minor:', latest.next_minor())
        print('next patch:', latest.next_patch())
    elif options.command == 'patch':
        print(latest.next_patch())
    elif options.command == 'minor':
        print(latest.next_minor())
    elif options.command == 'major':
        print(latest.next_major())




