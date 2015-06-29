from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='oreo',
    version='0.1',
    description='Ontology for REST Endpoints',
    long_description=long_description,
    url='https://github.com/utecht/oreo',
    author='Joseph Utecht',
    author_email='joseph.utecht@gmail.com',
    license='GPLv2',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3',
        ],
    keywords='REST RDF',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*'])
)
