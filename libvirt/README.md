# Ansible Playbook to Create KVM 

# Create

```bash
ansible-playbook -i inventory.ini kvm.yml
```

# Destroy

```bash
virsh -c qemu:///system destroy my-vm;  virsh -c qemu:///system undefine my-vm; rm -f /var/lib/libvirt/images/my-vm.qcow2
```
