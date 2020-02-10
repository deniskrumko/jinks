#!/usr/bin/env python3

from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='mrpl',
    version='0.0.1',
    description='CLI for opening links to JIRA-related things',
    long_description=readme,
    author='Denis Krumko',
    author_email='dkrumko@gmail.com',
    url='https://github.com/deniskrumko/jinks',
    license="MIT",
    entry_points={
        'console_scripts': [
            'jinks = jinks.main:main',
        ],
    },
    packages=['jinks'],
    python_requires=">=3.6",
    keywords='CLI, JIRA, links',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
    ],
)
