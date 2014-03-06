#!/usr/bin/env python

from setuptools import setup

setup(
    name='KFData.py',
    version='0.1.0',
    url='https://github.com/kylef/KFData.py',
    author='Kyle Fuller',
    author_email='inbox@kylefuller.co.uk',
    packages=('kfdata',),
    install_Requires=('jinja2'),
    entry_points={
        'console_scripts': (
            'kfdata = kfdata.manage:main',
        )
    },
    test_suite='kfdata.tests',
)

