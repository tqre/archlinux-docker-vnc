# Arch Linux host - making a template

These scripts create a ready configured Arch Linux in UpCloud
which can be templatized. An API enabled account is needed.
API calls will ask for your credentials.

Python scripts use getpass() to authenticate, it might hang
on virtual terminals/interpreters.

## Work in progress!

- root access is possible only via web console atm
- /etc/machine-id has to be resetted when cloning

Procedure:

1. Run deploy_arch.py
  - API call to set up an Arch Linux installation ISO
  - take note of the new server UUID 
2. Start the web-console and set up ad-hoc SSH connection:
  - set passwd for root
  - systemctl start sshd
  - SSH into the VM
3. Set variables in arch_host_install:
  - preferred mirror
  - timezone, locale, keyboard
  - hostname, username
  - SSH port number and public key
4. Run arch_host_install on the VM
  - This pretty much follows Arch Linux installation process
  - SSH is configured with key-only access for user
  - dhcp is set up with systemd
  - few GRUB customizations are made (random.trust and timeout 0)
  - server is shut down after settings are complete
5. Run config_and_restart.py
  - you need to set the server uuid manually for now
  - API call to change boot disk from cdrom to HD
  - API call to detach installation ISO
  - API call to start the VM
6. Everything done right, you can now SSH into the new machine

## Additional files:

arch_ISO.json
- installation ISO configuration for API call

bootfromHD.json
- API call body to change boot order

detachISO.json
- API call body to detach the Arch Linux installation ISO

## partition_map:

A here-document in arch_host_install for sfdisk partitioning:

Default scheme:

/dev/vda1 BIOS-boot 1M

/dev/vda2 / 8G

/dev/vda3 /home 17G

