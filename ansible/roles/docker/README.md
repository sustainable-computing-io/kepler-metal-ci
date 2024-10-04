Setup  Docker
=========

This role installs and configures Docker on both Metal and VM.

Role Variables
--------------

- `default/main.yml`:
  Default variables for this role.
- `vars/main.yml`:
  Variables defined in this file have higher precedence and are not intended to be overridden.
  - `bm_necessary_packages`: Packages necessary for Metal.
  - `vm_necessary_packages`: Packages necessary for VM.
  - `ubuntu_docker_gpg_key_url`: URL of the Ubuntu Docker GPG key(Metal).
  - `ubuntu_docker_repo_url`: URL of the Ubuntu Docker repository(Metal).
  - `fedora_docker_repo_url`: URL of the Fedora Docker repository(VM).
  - `docker_necessary_packages`: Packages necessary for Docker Installation.

Dependencies
------------

- VM should be created using the `kvm_vm` role.

License
-------

BSD
