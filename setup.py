# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import codecs
import re
from os import path

here = path.abspath(path.dirname(__file__))


def read(*parts):
    with codecs.open(path.join(here, *parts), 'r') as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='rtd_min_fail',
    version=find_version("rtd_min_fail", "__init__.py"),
    description="FPLO run evaluation",
    license='WTFPL',
    url='https://github.com/mueslo/rtd_min_fail',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[
        "numpy~=1.15",
        "matplotlib~=2.2",
    ],
    python_requires=">=2.7, <4",
    extras_require={
        'docs': ['sphinx', 'sphinx-gallery'],
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
)
