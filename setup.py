#!/usr/bin/env python
# coding:utf-8
from setuptools import setup, find_packages

# Setting up
setup(
    name="ashar",
    version='0.0.1',
    author="Yasser BDJ (Ro0t96)",
    author_email="by.root96@gmail.com",
    url="https://github.com/byRo0t96",
    maintainer='Yasser BDJ',
    maintainer_email='by.root96@gmail.com',
    description='ashar',
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    packages=find_packages(),
    project_urls={  # Optional
        'repositorie': 'https://github.com/byRo0t96/ashar',
    },
    install_requires=[],
    keywords=['python','ashar','encode','decode','key'],
    classifiers=[
        "Development Status :: 1 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
