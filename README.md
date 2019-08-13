[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

# Docker images for Hyperledger Aries Cloud Agent

The image repository is located [on Docker Hub](https://hub.docker.com/r/hyperledger/aries-cloudagent/).

The images include language-specific implementations of Aries Cloudagent such as:

-   [Aries CloudAgent Python (ACA-Py)](https://github.com/hyperledger/aries-cloudagent-python)

# Repository structure

The repository is structured so that there is a folder for each implementation/language , and this contains the dockerfiles and resources required to build and test the output image.

Inside [make_image.py] a data structure called `VERSIONS` describes the versions and base image for each implementation/language.

# Adding a new implementation/language

To add a new implementation/language:

1. create a new folder named after the new implementation in the root of the repository. For reference, the [python] folder can be copied and its contents updated to reflect the new implementation/language.
2. Update the `VERSIONS` object in [make_image.py] to add the new implementation/language details.

## Image versioning

All the `aries-cloudagent` images will reside on the [Aries Cloud Agent Docker Hub](https://hub.docker.com/r/hyperledger/aries-cloudagent/), and will differentiate between each other by using specific tags.

By default, the tag for a new image will be composed by `$base_image_tag`, followed by `_$agent_version`. Because of this naming convention, please make sure you use a tagged version for each base image rather than using `latest` or a more generic tag that is not as descriptive.

| Image tag         | indy-sdk                    | python | aries-cloudagent |
| ----------------- | --------------------------- | ------ | ---------------- |
| py36-1.11-0_0.3.0 | 1.11.0 with postgres plugin | 3.6    | 0.3.0            |

# Building the image locally

## Pre-requisites

To build the image locally you will need to install:

-   [Python 3](https://www.python.org/)
-   [Docker](https://www.docker.com/)

## Running the build

To build the image, open a terminal session at the root of this Git repo and execute: `python make_image.py python 0.3.0`.
This will build the python version of the image, and include aries-cloudagent version 0.3.0.

Many parameters can be specified through command-line, for more information please type `python make_image.py` to display the command's usage page.

# Credits

The build scripts in this repository have taken inspiration from the ones used to build [von-image](https://github.com/PSPC-SPAC-buyandsell/von-image)
