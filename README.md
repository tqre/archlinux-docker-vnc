# Archlinux docker images with VNC remote access
## work in progress...  
- experimenting with buildroot  
- got the basic tigervnc setup working on a full archlinux container and a shared desktop
- is it possible to containerize only x-server and just the programs needed (tigervnc)?  
- look into pacstrap/pacman solutions in creating a tarball for containerization
- cat ball.tar | docker import - <name>
- earlier solutions use host's xorg-server
- audio issues

This project is aiming to provide remote desktop access with container images.

Host is a cloud-based Arch Linux running docker. I'm hosting a server on UpCloud
as a testing environment. I have posted a guide how to install Arch Linux there:

https://upcloud.com/community/tutorials/install-arch-linux/

## Create a custom cloud-template:
### /host_template
- Convenience scripts to create and modify a vanilla Arch Linux template.
- set this up as a salt-minion?

## Set up docker images on a host VM

Containers are custom built, as a starting point, the following repo is used:

https://github.com/archlinux/archlinux-docker

Goal is to automate the whole dockerimage creation process with customizations
needed to provide a remote desktop environment.

## Docker image -server machine
- a VM that builds up-to-date docker images and serves the images to host VM's


Some further ideas/todos:  
Have a 3 tier system: dev,test,prod  
Configuration management: one salt-master to rule them all  
local package repository for pacman to reduce network consumption  
salt-cloud: Arch+Upcloud both missing, major work  
networking  
persistent storage  


