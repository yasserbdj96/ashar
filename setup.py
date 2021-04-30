#!/usr/bin/env python
# coding:utf-8
# code by : Yasser BDJ
# email : by.root96@gmail.com
#s
import os
from setuptools import setup, find_packages
from ashar.__version__ import __version__,__name__,__author__,__author_email__,__description__,__Author_WebSite__,__Source_Code__,__keywords__,__install_requires__,__license__,__copyright__

#read:
def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()

#__version__:
f=open('version.txt','w')
f.write(f"{__version__}")
f.close()

# Setting up:
setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=__description__,
    long_description_content_type="text/markdown",
    long_description=read("README.rst"),
    license=__license__,
    packages=find_packages(),
    project_urls={
        'Author WebSite':__Author_WebSite__,
        'Source Code':__Source_Code__,
    },
    install_requires=__install_requires__,
    keywords=__keywords__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        f"License :: OSI Approved :: {__license__}",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires=">=3.x.x"
)
#e