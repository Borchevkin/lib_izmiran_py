# Project Name

## Description

<<<<<<< HEAD
IZMIRAN library for common tasks
=======
IZMIRAN library for common tasks.
>>>>>>> feature/initial_20241008

## Documents

No additional documents are provided.

## Software Requirements

* Python 3.7+
* make

## Dependencies

* pytest
* yapf
* bandit

## Usage and installation

```bash
$ pip install izmiran
```

<<<<<<< HEAD
=======
***API is liquid due to development process. Use exact versioning!***

>>>>>>> feature/initial_20241008
## Developing Process

* Used feature-flow for developing

## Release Process

<<<<<<< HEAD
### Release Process - Steo 0 - Verify and validate codebase
=======
For preparing release needs only ti create 

### Release Process - Step 1 - Verify and validate codebase
>>>>>>> feature/initial_20241008

Run:

```bash
make all_release
```

### Release Process - Step 2 - Check installation of target

```bash
$ make install
```

### Release Process - Step 3 - Update version

Go to [pyproject.toml](./pyproject.toml) and [setup.py](./setup.py) and update `version`.

### Release Process - Step 4 - Update CHANGELOG.md

Go to `CHANGELOG.md` and update it.

### Release Process - Step 5 - Update package on PyPI

```bash
make publish
```
