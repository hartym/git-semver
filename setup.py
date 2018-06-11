# Generated by Medikit 0.6.3 on 2018-06-11.
# All changes will be overriden.
# Edit Projectfile and run “make update” (or “medikit update”) to regenerate.

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Py3 compatibility hacks, borrowed from IPython.
try:
    execfile
except NameError:

    def execfile(fname, globs, locs=None):
        locs = locs or globs
        exec(compile(open(fname).read(), fname, "exec"), globs, locs)


# Get the long description from the README file
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''

# Get the classifiers from the classifiers file
tolines = lambda c: list(filter(None, map(lambda s: s.strip(), c.split('\n'))))
try:
    with open(path.join(here, 'classifiers.txt'), encoding='utf-8') as f:
        classifiers = tolines(f.read())
except:
    classifiers = []

version_ns = {}
try:
    execfile(path.join(here, 'git_semver/_version.py'), version_ns)
except EnvironmentError:
    version = 'dev'
else:
    version = version_ns.get('__version__', 'dev')

setup(
    author='Romain Dorgueil',
    author_email='romain@dorgueil.net',
    description='Semantic versions management integrated to git.',
    license='Apache License, Version 2.0',
    name='git_semver',
    version=version,
    long_description=long_description,
    classifiers=classifiers,
    packages=find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data=True,
    install_requires=['GitPython (~= 2.1.7)', 'semantic-version (~= 2.6.0)'],
    extras_require={'dev': ['coverage (~= 4.4)', 'pytest (~= 3.4)', 'pytest-cov (~= 2.5)', 'sphinx (~= 1.7)', 'yapf']},
    entry_points={'console_scripts': ['git-semver=git_semver.__main__:main']},
    url='https://github.com/hartym/git-semver',
    download_url='https://github.com/hartym/git-semver/archive/{version}.tar.gz'.format(version=version),
)
