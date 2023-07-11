#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-fleetio",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_fleetio"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
    ],
    entry_points="""
    [console_scripts]
    tap-fleetio=tap_fleetio:main
    """,
    packages=["tap_fleetio"],
    package_data = {
        "schemas": ["tap_fleetio/schemas/*.json"]
    },
    include_package_data=True,
)
