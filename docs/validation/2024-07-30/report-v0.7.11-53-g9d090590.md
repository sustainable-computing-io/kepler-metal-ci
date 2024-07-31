# v0.7.11-53-g9d090590

## Build Info

  * `kepler_exporter_build_info{arch="amd64", branch="main", instance="localhost:8888", job="node", os="linux", revision="9d090590c35f8a025575622f6def1b008199b2f9", version="v0.7.11-53-g9d090590"}`
  * `kepler_exporter_build_info{arch="amd64", branch="main", instance="localhost:9999", job="vm", os="linux", revision="9d090590c35f8a025575622f6def1b008199b2f9", version="v0.7.11-53-g9d090590"}`
## Node Info

  * `kepler_node_info{components_power_source="rapl-sysfs", cpu_architecture="Coffee Lake", instance="localhost:8888", job="node", platform_power_source="acpi", source="os"}`
  * `kepler_node_info{components_power_source="estimator", cpu_architecture="Coffee Lake", instance="localhost:9999", job="vm", platform_power_source="none", source="os"}`
## Specs
### Host CPU Specs
| Model | Cores | Threads | Sockets | Flags |
|-----------|-----------|-------------|-------------|-----------|
| Intel(R) Xeon(R) E-2278G CPU @ 3.40GHz | 16 | 2 | 1 | ```fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp vnmi md_clear flush_l1d arch_capabilities``` |
### VM CPU Specs
| Model | Cores | Threads | Sockets | Flags |
|-----------|-----------|-------------|-------------|-----------|
| Intel(R) Xeon(R) E-2278G CPU @ 3.40GHz | 16 | 1 | 16 | ```fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon rep_good nopl xtopology cpuid tsc_known_freq pni pclmulqdq vmx ssse3 fma cx16 pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt xsaveopt xsavec xgetbv1 xsaves arat vnmi umip md_clear flush_l1d arch_capabilities``` |
### Host DRAM Size
| Size |
|------|
| 32582132 kB |
### VM DRAM Size
| Size |
|------|
| 32601200 kB |

## Validation Results

   * Started At: `2024-07-30 20:11:30.713426`
   * Ended   At: `2024-07-30 20:14:51.653984`
   * Duration  : `0:03:20.940558`

### Validate - platform - dynamic

  * expected:  `rate( kepler_node_platform_joules_total{ job="vm", mode="dynamic", }[20s] ) `
  * actual:  `rate( kepler_vm_platform_joules_total{ job="node", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
#### Errors

  * MSE: 1563.5053658130632
  * MAPE: inf
### Validate - package - dynamic

  * expected:  `rate( kepler_node_package_joules_total{ job="vm", mode="dynamic", }[20s] ) `
  * actual:  `rate( kepler_vm_package_joules_total{ job="node", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
#### Errors

  * MSE: 1083.6922467402715
  * MAPE: 60.67393557932456
### Validate - core - dynamic

  * expected:  `rate( kepler_node_core_joules_total{ job="vm", mode="dynamic", }[20s] ) `
  * actual:  `rate( kepler_vm_core_joules_total{ job="node", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
#### Errors

  * MSE: 1091.1548280274012
  * MAPE: 60.75980176020157
### Validate - dram - dynamic

  * expected:  `rate( kepler_node_dram_joules_total{ job="vm", mode="dynamic", }[20s] ) `
  * actual:  `rate( kepler_vm_dram_joules_total{ job="node", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
#### Errors

  * MSE: 23.694634566251384
  * MAPE: inf
### Validate - platform - idle

  * expected:  `rate( kepler_node_platform_joules_total{ job="vm", mode="idle", }[20s] ) `
  * actual:  `rate( kepler_vm_platform_joules_total{ job="node", vm_id=~".*my-vm", mode="idle", }[20s] ) `
#### Errors

  * MSE: 5674703129.572374
  * MAPE: 99.70742001673504
### Validate - package - idle

  * expected:  `rate( kepler_node_package_joules_total{ job="vm", mode="idle", }[20s] ) `
  * actual:  `rate( kepler_vm_package_joules_total{ job="node", vm_id=~".*my-vm", mode="idle", }[20s] ) `
#### Errors

  * MSE: 4867.900284382244
  * MAPE: 47523.47769246675
### Validate - core - idle

  * expected:  `rate( kepler_node_core_joules_total{ job="vm", mode="idle", }[20s] ) `
  * actual:  `rate( kepler_vm_core_joules_total{ job="node", vm_id=~".*my-vm", mode="idle", }[20s] ) `
#### Errors

  * MSE: 4871.2461412910125
  * MAPE: 56821.9317369549
### Validate - dram - idle

  * expected:  `rate( kepler_node_dram_joules_total{ job="vm", mode="idle", }[20s] ) `
  * actual:  `rate( kepler_vm_dram_joules_total{ job="node", vm_id=~".*my-vm", mode="idle", }[20s] ) `
#### Errors

  * MSE: 2218.006202263879
  * MAPE: 101473.68331973984
