from setuptools import setup, find_packages

setup(
    name="artifex",
    version="0.1",
    author="zignig",
    description="Pysible process builder",
    packages=find_packages(),
    project_urls={
        "Source Code": "https://github.com/zignig/artifex",
        "Bug Tracker": "https://github.com/zignig/artifex/issues",
    },
    entry_points={"console_scripts": ["artifex = artifex.cli:as_main"]},
)
