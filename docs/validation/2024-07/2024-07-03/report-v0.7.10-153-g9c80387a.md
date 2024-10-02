# v0.7.10-153-g9c80387a

## Build Info

  * `kepler_exporter_build_info{arch="amd64", branch="main", instance="localhost:8888", job="node", os="linux", revision="9c80387af3f9180fc10b5ab187d2e257453e1150", version="v0.7.10-153-g9c80387a"}`
  * `kepler_exporter_build_info{arch="amd64", branch="main", instance="localhost:9999", job="vm", os="linux", revision="9c80387af3f9180fc10b5ab187d2e257453e1150", version="v0.7.10-153-g9c80387a"}`
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
| 32750376 kB |
### VM DRAM Size
| Size |
|------|
| 32601864 kB |

## Validation Results

   * Started At: `2024-07-03 12:26:39.272944`
   * Ended   At: `2024-07-03 12:30:00.090260`
   * Duration  : `0:03:20.817316`

### Validate - platform - dynamic

  * expected:  `rate( kepler_node_platform_joules_total{ job="vm", mode="dynamic", }[20s] ) `
  * actual:  `rate( kepler_vm_platform_joules_total{ job="node", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
#### Errors

  * MSE: 1703976922.7341597
  * MAPE: 487219.28911450785
### Validate - package - dynamic

  * expected:  `rate( kepler_node_package_joules_total{ job="vm", mode="dynamic", }[20s] ) `
  * actual:  `rate( kepler_vm_package_joules_total{ job="node", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
#### Errors

  * MSE: 993307738.0310696
  * MAPE: 646612.9523778667
### Validate - core - dynamic

  * expected:  `rate( kepler_node_core_joules_total{ job="vm", mode="dynamic", }[20s] ) `
  * actual:  `rate( kepler_vm_core_joules_total{ job="node", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
#### Errors

  * MSE: 993312138.1768695
  * MAPE: 649023.9197322311
### Validate - dram - dynamic

  * expected:  `rate( kepler_node_dram_joules_total{ job="vm", mode="dynamic", }[20s] ) `
  * actual:  `rate( kepler_vm_dram_joules_total{ job="node", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
#### Errors

  * MSE: 25904207.959011428
  * MAPE: inf
### Validate - platform - idle

  * expected:  `rate( kepler_node_platform_joules_total{ job="vm", mode="idle", }[20s] ) `
  * actual:  `rate( kepler_vm_platform_joules_total{ job="node", vm_id=~".*my-vm", mode="idle", }[20s] ) `
#### Errors

  * MSE: 48340.65725742563
  * MAPE: 21150.991213118476
### Validate - package - idle

  * expected:  `rate( kepler_node_package_joules_total{ job="vm", mode="idle", }[20s] ) `
  * actual:  `rate( kepler_vm_package_joules_total{ job="node", vm_id=~".*my-vm", mode="idle", }[20s] ) `
#### Errors

  * MSE: 4866.211767659147
  * MAPE: 44809.07997919473
### Validate - core - idle

  * expected:  `rate( kepler_node_core_joules_total{ job="vm", mode="idle", }[20s] ) `
  * actual:  `rate( kepler_vm_core_joules_total{ job="node", vm_id=~".*my-vm", mode="idle", }[20s] ) `
#### Errors

  * MSE: 4868.916624713426
  * MAPE: 51296.1228361617
### Validate - dram - idle

  * expected:  `rate( kepler_node_dram_joules_total{ job="vm", mode="idle", }[20s] ) `
  * actual:  `rate( kepler_vm_dram_joules_total{ job="node", vm_id=~".*my-vm", mode="idle", }[20s] ) `
#### Errors

  * MSE: 2216.881476466062
  * MAPE: 81100.64311263563
