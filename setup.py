# setup.py
from setuptools import setup, find_packages

VERSION = "0.1"
DESCRIPTION = "Sri lanka APIT Calculation python library"
LONG_DESCRIPTION = "A package that makes it easy to calaclute Sri Lankan Advance Personal Income Tax (APIT Tax)"

setup(
    name="apit_lk",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Dinuth Perera",
    author_email="pm@dinuth.me",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    tests_require=["unittest"],
    test_suite="tests",
    keywords="conversion",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
)
