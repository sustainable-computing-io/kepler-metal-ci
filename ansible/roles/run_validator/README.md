Run Validator
==============

This role runs the validator tool on the Metal

Role Variables
--------------

- `default/main.yml`:
  Default variables for this role.
  - `log_level`: Log level for the validator. Default is `info`.
  - `prometheus_url`: URL of the Prometheus server. Default is `http://localhost:9090`.
  - `rate_interval`: Rate interval for the validator. Default is `20s`.
  - `steps`: Steps for the validator. Default is `5s`.
- `vars/main.yml`:
  Variables defined in this file have higher precedence and are not intended to be overridden.
  - `validator_dir`: Directory where the validator is located.
  - `validator_yaml_path`: Path to the validator YAML file.

Dependencies
------------

- VM should be created using the `kvm_vm` role.
- Docker should be installed on the VM using the `setup_docker` role.
- Kepler should be installed on the VM using the `install_kepler` role.

License
-------

BSD
