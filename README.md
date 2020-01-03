# Archlinux docker images with VNC remote access
## work in progress...

This project is aiming to provide remote desktop access with container images.

Host is a cloud-based Arch Linux running docker. I'm hosting a server on UpCloud
as a testing environment. I have posted a guide how to install Arch Linux there:

https://upcloud.com/community/tutorials/install-arch-linux/

## Create a custom cloud-template:
### /host_template
- Convenience scripts to create and modify a vanilla Arch Linux template.

## Set up docker images on a host VM

Containers are custom built, as a starting point, the following repo is used:

https://github.com/archlinux/archlinux-docker

Goal is to automate the whole dockerimage creation process with customizations
needed to provide a remote desktop environment.

Some further ideas:
Have a 3 stage system: dev,test,prod
Configuration management: one salt-master to rule them all


