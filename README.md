# ToolKitten

Library of utilities for visualization, analytics and ML.
Contains basic functions for mathematics, graphs and statistics.

## Documentation

You can run documentation via mkdocs:

```commandline
$ mkdocs serve -a localhost:8000
OR
$ poetry run mkdocs serve -a localhost:8000
```

## Build and Install

### Build the Package

To build the package, make sure you have [Poetry](https://python-poetry.org/) installed. 
If not, you can install it by running:

```bash
$ pip install poetry
```

After that, navigate to the root of the project and run the following command to build the package:

```bash
$ poetry build
```

This will generate two distribution files in the dist directory:
- A `.tar.gz` source distribution
- A `.whl` wheel distribution

### Install the Package
Once the build process is complete, you can install the package using `pip` from the dist folder.

Navigate to the dist folder:

```bash
$ cd dist
```

To install the `.whl` file (recommended for faster installation), run:

```bash
$ pip install toolkitten-0.0.1-py3-none-any.whl
```

Or, if you prefer to install the source distribution as `.tar.gz`, run:

```bash
$ pip install toolkitten-0.0.1.tar.gz
```

### Verify Installation
After installing, you can verify that the package has been installed correctly by running:

```bash
$ pip show toolkitten
```

This will display information about the installed package, including its version.