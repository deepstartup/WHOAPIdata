#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Arghadeep1990",
    version="0.0.1",
    author="Arghadeep Chaudhury,Siddhartha Bhattacharya",
    author_email="siddhartha.bhattacharya@in.ibm.com,arghadeep.chaudhury@gmail.com",
    description="Getting the world helth organization data using who api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deepstartup/WHOAPIdata",
    packages=find_packages(),
    install_requires=['pandas', 'requests', 'json', 'json2xml'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)