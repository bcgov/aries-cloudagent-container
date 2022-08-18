[![img](https://img.shields.io/badge/Lifecycle-Stable-97ca00)](https://github.com/bcgov/repomountie/blob/master/doc/lifecycle-badges.md)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

# Docker images for Hyperledger Aries Cloud Agent

The image repository is located [on Docker Hub](https://hub.docker.com/r/bcgovimages/aries-cloudagent/).

The images include language-specific implementations of Aries Cloudagent such as:

-   [Aries CloudAgent Python (ACA-Py)](https://github.com/hyperledger/aries-cloudagent-python)

# Repository structure

The repository is structured so that there is a folder for each implementation/language , and this contains the dockerfiles and resources required to build and test the output image.

Inside [make_image.py](make_image.py#L10) a data structure called `VERSIONS` describes the versions and base image for each implementation/language.

# Adding a new implementation/language

To add a new implementation/language:

1. create a new folder named after the new implementation in the root of the repository. For reference, the [python](python) folder can be copied and its contents updated to reflect the new implementation/language.
2. Update the `VERSIONS` object in [make_image.py](make_image.py#L10) to add the new implementation/language details.

## Image versioning

All the `aries-cloudagent` images will reside on the [Aries Cloud Agent Docker Hub](https://hub.docker.com/r/bcgovimages/aries-cloudagent/), and will differentiate between each other by using specific tags.

By default, the tag for a new image will be composed by `$base_image_tag`, followed by `_$agent_version`. Because of this naming convention, please make sure you use a tagged version for each base image rather than using `latest` or a more generic tag that is not as descriptive.

| Image tag         | Implementation | Base image            | aries-cloudagent |
| ----------------- | -------------- | --------------------- | ---------------- |
| py36-1.11-0_0.3.0 | python         | von-image:py36-1.11-0 | 0.3.0            |
| py36-1.11-0_0.3.1 | python         | von-image:py36-1.11-0 | 0.3.1            |
| py36-1.11-1_0.3.2 | python         | von-image:py36-1.11-1 | 0.3.2            |
| py36-1.11-1_0.3.3 | python         | von-image:py36-1.11-1 | 0.3.3            |
| py36-1.11-1_0.3.4 | python         | von-image:py36-1.11-1 | 0.3.4            |
| py36-1.11-1_0.3.5 | python         | von-image:py36-1.11-1 | 0.3.5            |
| py36-1.11-1_0.4.0 | python         | von-image:py36-1.11-1 | 0.4.0            |
| py36-1.11-1_0.4.1 | python         | von-image:py36-1.11-1 | 0.4.1            |
| py36-1.14-0_0.4.2 | python         | von-image:py36-1.14-0 | 0.4.2            |
| py36-1.14-1_0.4.3 | python         | von-image:py36-1.14-1 | 0.4.3            |
| py36-1.14-1_0.4.4 | python         | von-image:py36-1.14-1 | 0.4.4            |
| py36-1.14-1_0.4.5 | python         | von-image:py36-1.14-1 | 0.4.5            |
| py36-1.14-1_0.5.0 | python         | von-image:py36-1.14-1 | 0.5.0            |
| py36-1.14-1_0.5.1 | python         | von-image:py36-1.14-1 | 0.5.1            |
| py36-1.15-0_0.5.2 | python         | von-image:py36-1.15-0 | 0.5.2            |
| py36-1.15-0_0.5.3 | python         | von-image:py36-1.15-0 | 0.5.3            |
| py36-1.15-0_0.5.4 | python         | von-image:py36-1.15-0 | 0.5.4            |
| py36-1.15-0_0.5.5 | python         | von-image:py36-1.15-0 | 0.5.5            |
| py36-1.15-0_0.5.6 | python         | von-image:py36-1.15-0 | 0.5.6            |
| py36-1.15-1_0.6.0 | python         | von-image:py36-1.15-1 | 0.6.0            |
| py36-1.16-1_0.7.0 | python         | von-image:py36-1.16-1 | 0.7.0            |
| py36-1.16-1_0.7.1 | python         | von-image:py36-1.16-1 | 0.7.1            |
| py36-1.16-1_0.7.2 | python         | von-image:py36-1.16-1 | 0.7.2            |
| py36-1.16-1_0.7.3 | python         | von-image:py36-1.16-1 | 0.7.3            |
| py36-1.16-1_0.7.4 | python         | von-image:py36-1.16-1 | 0.7.4            |
| py36-1.16-1_1.0.0-rc0 | python     | von-image:py36-1.16-1 | 1.0.0-rc0        |

# Building the image locally

This project is setup to use **Visual Studio Code Remote - Containers**.  The devContainer includes everything you need to work on the project and build the images.  The container uses docker-from-docker so any images you build will show up in your host's docker repository.

## Pre-requisites

Using the devContainer:

- Visual Studio Code with the Remote - Containers extension installed.
- [Docker](https://www.docker.com/)

To develop and build the image locally you will need to install:

- [Python 3](https://www.python.org/)
- [Docker](https://www.docker.com/)

## Running the build

To build the image, open a terminal session at the root of this git repo and execute: `python make_image.py 0.3.0 python`,
replacing `0.3.0` with the aries-cloudagent version you need.

Additional parameters can be specified through command-line, for more information please type `python make_image.py --help` to display the command's usage page.

## Building an image from a GitHub source

In some cases you may want to build an image from a particular repository and branch.  You can do this by adding the `git_egg_ref` build-arg to the command line.  In this case the version number you specify will only be used to determine the relevant `base_image` and `acapy_reqs` to use for the build.

The format of the `git_egg_ref` argument is:
- `git+`**<git_repo_url>**[`@`**<git_ref>**]`#egg=`
  - Where:
    - **<git_repo_url>**: Is the url to the repo including the trailing `.git` extension.
    - **<git_ref>**: Optional.  The `git_ref` of the branch or tag to use.  If specified, the `<git_repo_url>` and `<git_ref>` must be separated by a `@`.

Example:
```
./make_image.py 0.7.3 python --build-arg git_egg_ref="git+https://github.com/WadeBarnes/aries-cloudagent-python.git@persistant_queue#egg="
```
## Adding and Publishing a New Image

To add a new version of aries-cloudagent to this repo, create a PR with the following changes:

- Decide on the base image to be used for the image, and the version of Aries Cloud Agent.
  - The image tag of the output will be a concatenation of the two, as indicated in the table above.
- Update the table in this readme to add the new version.
- Edit the [make_image.py](make_image.py) file in this repo to add the new version.
- Create and test the build of the local image using the options `--no-cache` and `--test`
  - `python make_image.py 0.7.2-rc0 --no-cache --test python`
- If successful, push the image to the bcgovimages organization of Docker Hub using the `--push` option
  - `python make_image.py 0.7.2-rc0 --push python`
- If successful, verify the publishing of the image by checking [Docker Hub](https://hub.docker.com/r/bcgovimages/aries-cloudagent/tags)
  - Note that it make take a few minutes for the new tag to appear. Hit refresh periodically until the image is visible.

# Credits

The build scripts in this repository have taken inspiration from the ones used to build [von-image](https://github.com/PSPC-SPAC-buyandsell/von-image)
