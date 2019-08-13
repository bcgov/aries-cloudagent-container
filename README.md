[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

# Docker images for Hyperledger Aries Cloud Agent

The image repository is located [on Docker Hub](https://hub.docker.com/r/hyperledger/aries-cloudagent/).

The images include:

-   [Aries CloudAgent Python (ACA-Py)](https://github.com/hyperledger/aries-cloudagent-python)
-   [Hyperledger Indy SDK](https://github.com/hyperledger/indy-sdk) and Indy CLI
-   [Hyperledger Indy Node](https://github.com/hyperledger/indy-node)
-   [Python](https://www.python.org/)

# Building the image locally

## Pre-requisites

To build the image locally you will need to install:

-   [Python 3](https://www.python.org/)
-   [Docker](https://www.docker.com/)

## Running the build

To build the image, open a terminal session at the root of this Git repo and execute: `python make_image.py 0.3.0`. This will build the image using version aries-cloudagent version 0.3.0.

Many parameters can be specified through command-line, for more information please type `python make_image.py` to display the command's usage page.

# Credits

The build scripts in this repository have taken inspiration from the ones used to build [von-image](https://github.com/PSPC-SPAC-buyandsell/von-image)
