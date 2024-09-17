Deploy VM
=========

This role deploys and configure VM on Metal.

Role Variables
--------------

- `default/main.yml`:
  Default variables for this role.
- `vars/main.yml`:
  Variables defined in this file have higher precedence and are not intended to be overridden.
  - `vcpu_count`: Number of vCPUs for the VM. Default is `14`.
  - `memory_size`: Memory size for the VM. Default is `16384`(MB).
  - `cpu_pinning`: CPU pinning for the VM. Default is `1-7,9-15`.
  - `isolated_cores`: Isolated cores for the VM. Default is `1-7,9-15`.
  - `vm_name`: Name of the VM.
  - `vm_disk_path`: Path to the VM disk.
  - `ssh_key_path`: Path to the SSH key.
  - `backup_vm_disk_path`: Path to the backup VM disk.
  - `vm_image_url`: URL of the VM image.(Fedora 40)
  - `vm_user`: Username for the VM.
  - `vm_password`: Password for the VM.
  - `ssh_pub_key_path`: Path to the SSH public key.
  - `cloud_init_config_path`: Path to the Cloud-Init configuration file.
  - `packages`: Packages required for VM configuration on Metal.

Dependencies
------------

- Metal should be up and running

License
-------

BSD
