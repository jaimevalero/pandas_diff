#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Jaime Valero",
    author_email='jaimevalero78@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python utility to extract differences between two pandas dataframes.",
    entry_points={
        'console_scripts': [
            'pandas_diff=pandas_diff.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pandas_diff',
    name='pandas_diff',
    packages=find_packages(include=['pandas_diff', 'pandas_diff.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jaimevalero/pandas_diff',
    version='0.7.13',
    zip_safe=False,
)
