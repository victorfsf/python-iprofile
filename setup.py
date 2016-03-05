# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

version = '0.3.3'


setup(
    name='python-iprofile',
    packages=find_packages(exclude=['tests']),
    package_data={
        'iprofile': [],
    },
    install_requires=[
        'click==6.2',
        'glob2==0.4.1',
        'ipython>=4.0.0',
        'python-slugify==1.2.0',
        'PyYAML==3.11',
        'six==1.10.0',
    ],
    zip_safe=False,
    version=version,
    description='A CLI for handling IPython 4+ profiles startup scripts.',
    author='Victor Ferraz',
    author_email='victorfsf.dev@gmail.com',
    url='https://github.com/victorfsf/python-iprofile',
    keywords=[
        'ipython',
        'ipython4',
        'python',
        'python2',
        'python3',
        'shell',
        'profile',
        'iprofile',
        'django',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
    ],
    entry_points={
        'console_scripts': [
            'iprofile = iprofile.console:main',
        ],
    }
)
