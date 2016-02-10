# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

version = '0.1.1b'


setup(
    name='python-iprofile',
    packages=find_packages(exclude=['tests']),
    package_data={
        'iprofile': [],
    },
    install_requires=[
        'click==6.2',
        'ipython>=4',
        'python-slugify==1.2.0'
    ],
    zip_safe=False,
    version=version,
    description='A CLI for handling IPython 4+ profiles startup scripts.',
    author='Victor Ferraz',
    author_email='victorfsf.dev@gmail.com',
    url='https://github.com/victorfsf/python-iprofile',
    keywords=[
        'ipython',
        'python',
        'python2',
        'python3',
        'shell',
        'profile',
        'iprofile'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            'iprofile = iprofile.console:main',
        ],
    }
)
