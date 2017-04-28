from __future__ import print_function
from setuptools import setup, find_packages
import sys
import re
import ast


if sys.version_info <= (2, 7):
    error = "ERROR: words2num requires Python 2.7 or later"
    print(error, file=sys.stderr)
    sys.exit(1)

with open('README.md') as f:
    long_description = f.read()

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('words2num/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name="words2num",
    version=version,
    description="Inverse text normalization for numbers",
    long_description=long_description,
    author="Joshua Dong",
    author_email="jdong42@gmail.com",
    url="http://github.com/JDongian/python-words2num",
    install_requires=[
    ],
    packages=find_packages(),
)
