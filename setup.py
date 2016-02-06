# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

version = '0.0.1'


setup(
    name='python-iprofile',
    packages=find_packages(exclude=['tests']),
    package_data={
        'iprofile': [],
    },
    install_requires=[
        'ipython>=4',
        'glob2==0.4.1',
        'click==6.2'
    ],
    zip_safe=False,
    version=version,
    description='A CLI for handling IPython 4+ profiles startup scripts.',
    author='Victor Ferraz',
    author_email='victorfsf.dev@gmail.com',
    url='https://github.com/victorfsf/python-iprofile',
    download_url='',
    keywords=[
        'ipython',
        'python',
        'python2',
        'shell',
        'profile',
        'iprofile'
    ],
    entry_points={
        'console_scripts': [
            'iprofile = iprofile.console:main',
        ],
    }
)
