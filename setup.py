from setuptools import setup, find_packages

setup(
    name="izmiran",
    version="0.1.0",
    description=
    "IZMIRAN module for common tasks",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD 2-Clause License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)