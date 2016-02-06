# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


setup(
    name='python-iprofile',
    packages=find_packages(exclude=['tests']),
    package_data={
        'python-iprofile': [],
    },
    install_requires=[
        'glob2==0.4.1',
        'click==6.2'
    ],
    zip_safe=False,
    version='0.0.1',
    description='A IPython 4+ Profiles CLI tool',
    author='Victor Ferraz',
    author_email='vfsf@cin.ufpe.br',
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
