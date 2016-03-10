[![PyPI](https://img.shields.io/pypi/pyversions/vispr.svg?style=flat-square)]()
[![PyPI](https://img.shields.io/pypi/v/vispr.svg?style=flat-square)](https://pypi.python.org/pypi/vispr)
[![bioconda-badge](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat-square)](http://bioconda.github.io)
[![PyPI](https://img.shields.io/pypi/dw/VISPR.svg?style=flat-square)](https://pypi.python.org/pypi/vispr)
[![Anaconda-Server Badge](https://anaconda.org/bioconda/vispr/badges/downloads.svg)](https://anaconda.org/bioconda/vispr)

VISPR - A visualization framework for CRISPR data.
==================================================

VISPR is a web-based, interactive visualization framework for CRISPR/Cas9 knockout screen experiments.
For recent changes, see the [change log](CHANGELOG.md).

Installation
------------

The easiest way to install VISPR is to use the **Miniconda3** Python distribution (http://conda.pydata.org/miniconda.html). Make sure you install the Python 3 variant.
On Linux or Mac OSX, you can then issue

    conda install --channel bioconda vispr

in a **terminal** to install VISPR with all dependencies using the [Bioconda channel](http://bioconda.github.io).

To update VISPR and all other installed Conda packages, issue

    conda update --channel bioconda --all

If you are using an old version of MacOS X and the `conda` command is not available after installation of Miniconda, you have to change your shell to `bash`. To do this permanently, issue

    chsh -s /bin/bash

Usage
-----

All steps below have to be executed in a **terminal**.

### Step 1: Testing VISPR

After successful installation, you can test VISPR with example data by executing

    vispr test

in a terminal. This will download test data and allow you to explore all features of VISPR.

### Step 2: Configuring VISPR

VISPR takes [MAGeCK](http://liulab.dfci.harvard.edu/Mageck) and [FastQC](http://www.bioinformatics.babraham.ac.uk/projects/fastqc) results as input.
To display such results in VISPR, you have to provide a config file that points to result files and sets additional parameters. One config file defines one set of results (i.e. one experiment).
The easiest way to generate your own data and create vispr config files is to use the [MAGeCK-VISPR](https://bitbucket.org/liulab/mageck-vispr) workflow.
If you don't want to use the workflow, you can manually create a VISPR config by issueing

    vispr config

to obtain a template for modification.

### Step 3: Running VISPR

Once you have a config file (either generated by the workflow or manually), you can issue

    vispr server path/to/config.yaml

to start a server process that renders the VISPR user interface in a webbrowser.
VISPR can be invoked with multiple config files (i.e. multiple experiments), allowing to select and compare experiments via the user interface.

Further, you can compress results into an archive that can easily be sent via email:

    vispr archive path/to/config.yaml myexperiment.tar.bz2

Then, even on a different workstation, the results can be extracted and visualized with VISPR:

    tar -xf myexperiment.tar.bz2
    vispr server myexperiment/vispr.yaml

For further help, explore all command line options of VISPR with

    vispr --help

Author
------

Johannes Köster <koester@jimmy.harvard.edu>

License
-------

Licensed under the MIT license (http://opensource.org/licenses/MIT). This project may not be copied, modified, or distributed except according to those terms.