"""
Setup script for the Subnet CLI Calculator package.
"""

from setuptools import setup
import re
import os

# Read version from main.py
def get_version():
    with open("main.py", "r") as f:
        content = f.read()
        version_match = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", content)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string")

# Read README for long description
def get_long_description():
    if os.path.exists("README.md"):
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    return "Subnet CLI Calculator for CIDR subnetting and subnet mask calculations."

setup(
    name="subnet-cli-calculator",
    version=get_version(),
    author="Matan Shabi",
    author_email="matan.shabi20@gmail.com",
    description="A CLI tool for subnetting and subnet mask calculations",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/Matan-Shabi/msd-pipiline-hw",
    py_modules=["main"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "flake8",
            "bandit",
            "safety",
        ],
    },
    entry_points={
        "console_scripts": [
            "subnet-calc=main:main",
        ],
    },
)
