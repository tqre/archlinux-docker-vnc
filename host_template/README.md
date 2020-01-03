# Arch Linux host - making a template

These scripts create a ready configured Arch Linux in UpCloud
which will be templatized. An API enabled account is needed.
API calls will ask for your credentials.

Python scripts use getpass() to authenticate, it might hang
on IDE virtual environments.

## Work in progress!

- /etc/machine-id gets duplicated
- pacman keyring in /etc/pacman.d gets duplicated

Procedure:

1. Run deploy_arch.py
  - API call to set up an Arch Linux installation ISO
  - take note of the new server UUID 
    - TODO: VM UUID, storage UUID's generated -> store somewhere
2. Start the web-console and set up ad-hoc SSH connection:
  - set passwd for root
  - systemctl start sshd
  - SSH into the VM
3. Set variables in arch_host_install:
  - preferred mirror
  - timezone, locale, keyboard
  - hostname, username, password
  - SSH port number and public key
    - TODO: partition_map could be separate file
4. Run arch_host_install on the VM
  - follows Arch Linux installation process
  - SSH is configured with key-only access for user
  - dhcp is set up with systemd
  - GRUB/kernel cmdline customizations: random.trust and timeout 0
  - last chance to change password before templatizing
  - server is shut down after settings are complete
5. Run templatize.py
  - you need to set the server uuid manually for now
  - API call to change boot disk from cdrom to HD
  - API call to detach installation ISO
  - API call to make a custom template from the created server
  - API call to make one clone from the template
  - API call to delete the original templatized VM

## Additional files:

arch_ISO.json
- installation ISO configuration for API call

bootfromHD.json
- API call body to change boot order

detachISO.json
- API call body to detach the Arch Linux installation ISO

clones.json
- API call body for making clones of the created template


## partition_map:

A here-document in arch_host_install for sfdisk partitioning:

Default scheme:
```
/dev/vda1 BIOS-boot 1M  
/dev/vda2 / 8G  
/dev/vda3 /home 17G  
```

