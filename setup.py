from __future__ import print_function
from setuptools import setup, find_packages
from word2num import __version__
import sys


if sys.version_info <= (3, 0):
    error = "ERROR: word2num requires Python 3.0 or later"
    print(error, file=sys.stderr)
    sys.exit(1)

with open('README.md') as f:
    long_description = f.read()

setup(
    name="word2num",
    version=__version__,
    description="Inverse text normalization for numbers",
    long_description=long_description,
    author="Joshua Dong",
    author_email="jdong42@gmail.com",
    url="http://github.com/JDongian/python-word2num",
    install_requires=[
    ],
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Pre-Alpha",
        "Intended Audience :: Data Scientists",
        "Operating System :: OS Independent",
        "Topic :: Natural Language Processing",
        "Programming Language :: Python :: 3",
    ],
)
