# Docker Image construction scripts for Arch Linux remote desktop project
Originally cloned from https://github.com/archlinux/archlinux-docker  
This repository contains all scripts and files needed to create a Docker base image for the Arch Linux distribution.  

These images are run under host_template created VM's to provide a vnc remote desktop.  
A separate machine can be used to construct the images, then provide the latest image to the VM's.  

TODO: test scripts, explain all reasons, get packages

## Build dependencies
Install the following Arch Linux packages:
* make
* devtools
* docker
## Usage
Run `make docker-image` as root to build the base image.
## Purpose (to be redefined)
* Provide the Arch experience in a Docker Image
* Provide the most simple but complete image to base every other upon
* `pacman` needs to work out of the box
* All installed packages have to be kept unmodified
