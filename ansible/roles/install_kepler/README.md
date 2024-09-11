Install Kepler
=========

This role installs Kepler on both Metal and VM using Compose manifests that are available in the [Kepler repository](https://github.com/sustainable-computing-io/kepler/tree/main/manifests/compose/validation).

Role Variables
--------------

- `default/main.yml`:
  Default variables for this role.
  - `subnet`: Subnet for the VM. Default is `192.168.122.0/24`.
- `vars/main.yml`:
  Variables defined in this file have higher precedence and are not intended to be overridden.
  - `kepler_repo`: URL of the Kepler repository.
  - `kepler_dir`: Directory where Kepler repo is cloned.
  - `metal_compose_dir`: Directory where Metal Compose manifests are located.
  - `vm_compose_dir`: Directory where VM Compose manifests are located.

Dependencies
------------

- VM should be created using the `kvm_vm` role.
- Docker should be installed on the VM using the `setup_docker` role.

License
-------

BSD
