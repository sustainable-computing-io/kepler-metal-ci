Kepler Installation via Systemd
=========

This role installs Kepler on Metal and VM using systemd.

Role Variables
--------------

- `defaults/main.yml`: Default variables for this role
- `vars/main.yml`: Variables defined in this file has higher precedence and are not intended to be overridden
  - `kepler_image`: The image to use for Kepler

Dependencies
------------

- VM should be created using the `kepler_vm` role

License
-------

BSD
