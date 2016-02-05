# -*- coding: utf-8 -*8-

from setuptools import setup
from setuptools import find_packages


setup(
    name='python-ishell',
    packages=find_packages(exclude=['tests']),
    package_data={
        'ishell': [],
    },
    install_requires=[
        'glob2==0.4.1',
    ],
    zip_safe=False,
    version='0.0.1',
    description='TODO',
    author='Victor Ferraz',
    author_email='vfsf@cin.ufpe.br',
    url='https://github.com/victorfsf/python-ishell',
    download_url='',
    keywords=[
        'ipython',
        'python',
        'python2',
        'shell',
        'profile'
    ],
    entry_points={
        'console_scripts': [
            'ishell = ishell',
        ],
    }
)
