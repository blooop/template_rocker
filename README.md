# template_rocker

This has basic setup for

* pylint
* ruff
* black
* pytest
* git-lfs
* basic github actions ci
* pulling updates from this template
* codecov
* pypi upload
* dependabot

## Continuous Integration Status

[![Ci](https://github.com/blooop/template_rocker/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/blooop/template_rocker/actions/workflows/ci.yml?query=branch%3Amain)
[![Codecov](https://codecov.io/gh/blooop/template_rocker/branch/main/graph/badge.svg?token=Y212GW1PG6)](https://codecov.io/gh/blooop/template_rocker)
[![GitHub issues](https://img.shields.io/github/issues/blooop/template_rocker.svg)](https://GitHub.com/blooop/template_rocker/issues/)
[![GitHub pull-requests merged](https://badgen.net/github/merged-prs/blooop/template_rocker)](https://github.com/blooop/template_rocker/pulls?q=is%3Amerged)
[![GitHub release](https://img.shields.io/github/release/blooop/template_rocker.svg)](https://GitHub.com/blooop/template_rocker/releases/)
[![License](https://img.shields.io/github/license/blooop/template_rocker
)](https://opensource.org/license/mit/)
[![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/downloads/)
[![Pixi Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json)](https://pixi.sh)

## Intro

This is a [rocker](https://github.com/tfoote/rocker) extension for adding [pixi](https://pixi.sh) to a docker container.  Look at the [rocker](https://github.com/osrf/rocker) github page for more context of how [rocker](https://github.com/osrf/rocker) and [rocker](https://github.com/osrf/rocker) extensions work, but in a nutshell rocker lets you add custom capabilities to existing docker containers.  Rocker extensions   

[Pixi](https://github.com/prefix-dev/pixi) is a cross-platform package manager based on the conda ecosystem.  It provides a simple and performant way of reproducing a development environment and running user defined tasks and worflows.  It more lightweight than docker, but does not provide the same level of isolation or generality. 

1. Use github to use this project as a template
2. Clone the project and run, `scripts/update_from_template.sh` and then run the `scripts/rename_project.sh` to rename the project.

The most common question I get is is why would you need to use pixi in docker as pixi is already taking care of your environment for you.  Unfortunately there are some packages/configuration that pixi is not able to handle yet and so one way of handling that is managing those dependencies/configuration in docker and leave the the rest up to pixi. 

If you are using pixi, look at the available tasks in pyproject.toml  If you are new to pixi follow the instructions on the pixi [website](https://prefix.dev/)

# Github setup

There are github workflows, for CI, codecov and automated pypi publishing in `ci.yml` and `publish.yml`.

ci.yml uses pixi tasks to set up the environment matrix and run the various CI tasks. To set up codecov on github, you need to get a `CODECOV_TOKEN` and add it to your actions secrets.

publish.yml uses [pypy-auto-publish](https://github.com/marketplace/actions/python-auto-release-pypi-github) to automatically publish to pypi if the package version number changes. You need to add a `PYPI_API_TOKEN` to your github secrets to enable this.     

If you use vscode to attach to your development container it makes it easier to set up specific extensions for each project that don't need to be installed globally. 

## Installation

There are currently two ways of running code.  The preferred way is to use pixi to manage your environment and dependencies. 

```bash
cd project

$pixi run ci
pixi run arbitrary_task
```

If you have dependencies or configuration that cannot be managed by pixi, you can use alternative tools:

- [rockerc](https://github.com/blooop/rockerc): A command-line tool for dynamically creating docker containers with access to host resources such as GPU and 
- [rockervsc](https://github.com/blooop/rockervsc): A Visual Studio Code extension that integrates rockerc functionality into [vscode remote containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

These tools help you create isolated environments with specific dependencies, ensuring consistent setups across different machines.

```bash
cd project_name

rockerc # build and launch container with dependencies set up
# OR
rockervsc # build container, launch and attach vscode to that container.

#once you are inside the container you can use the pixi workflows.
pixi run ci
```

## Legacy

If you don't want to install rocker on your system but want to use vscode, you can run the `scripts/launch_vscode.sh` script to build and connect to a docker container. It will install rocker in a venv.  The docker container is dynamically generated using [rocker](https://github.com/osrf/rocker) and [deps rocker](https://github.com/blooop/deps_rocker).  [deps rocker](https://github.com/blooop/deps_rocker) looks at the python_template.deps.yaml file to install any required apt, pip or shell scripts and launches a container that vscode attaches to. 

## Troubleshooting

The main pixi tasks are related to CI.  Github actions runs the pixi task "ci".  The CI is mostly likey to fail from a lockfile mismatch.  Use the "fix" task to fix any lockfile related problems. 

## vscode tasks

There are two core tasks.  

1. set \<cfg\> from active file

    This sets \<cfg\> to the currently opened file in the editor

2. run \<cfg\>

    This runs python with the file set in \<cfg\>

To install pixi in a container use the --pixi flag

```
#add pixi to the ubuntu:22.04 image
rocker --pixi ubuntu:22.04

# add pixi to the nvidia/cuda image
rocker --pixi nvidia/cuda
```
