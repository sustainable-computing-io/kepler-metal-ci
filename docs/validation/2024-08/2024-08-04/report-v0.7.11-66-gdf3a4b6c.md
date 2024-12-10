# v0.7.11-66-gdf3a4b6c

## Build Info

  * `kepler_exporter_build_info{arch="amd64", branch="main", instance="localhost:8888", job="metal", os="linux", revision="df3a4b6c488770b6cc0a5410db2fb2ed689e98e2", version="v0.7.11-66-gdf3a4b6c"}`
  * `kepler_exporter_build_info{arch="amd64", branch="main", instance="localhost:9999", job="vm", os="linux", revision="df3a4b6c488770b6cc0a5410db2fb2ed689e98e2", version="v0.7.11-66-gdf3a4b6c"}`
## Node Info

  * `kepler_node_info{components_power_source="rapl-sysfs", cpu_architecture="Coffee Lake", instance="localhost:8888", job="metal", platform_power_source="acpi", source="os"}`
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
| 32582128 kB |
### VM DRAM Size
| Size |
|------|
| 32601196 kB |

## Validation Results

   * Started At: `2024-08-04 12:13:53.213079`
   * Ended   At: `2024-08-04 12:17:13.983251`
   * Duration  : `0:03:20.770172`

### Validate - platform - dynamic

  * expected:  `rate( kepler_node_platform_joules_total{ job="vm", mode="dynamic", }[20s] ) `
  * actual:  `rate( kepler_vm_platform_joules_total{ job="metal", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
#### Errors

  * MSE: 5838.581987209413
  * MAPE: inf
### Validate - package - dynamic

  * expected:  `rate( kepler_node_package_joules_total{ job="vm", mode="dynamic", }[20s] ) `
  * actual:  `rate( kepler_vm_package_joules_total{ job="metal", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
#### Errors

  * MSE: 1468.2398372844932
  * MAPE: 13201.413629144832
### Validate - core - dynamic

  * expected:  `rate( kepler_node_core_joules_total{ job="vm", mode="dynamic", }[20s] ) `
  * actual:  `rate( kepler_vm_core_joules_total{ job="metal", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
#### Errors

  * MSE: 1466.7526321683167
  * MAPE: 13077.92885906412
### Validate - dram - dynamic

  * expected:  `rate( kepler_node_dram_joules_total{ job="vm", mode="dynamic", }[20s] ) `
  * actual:  `rate( kepler_vm_dram_joules_total{ job="metal", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
#### Errors

  * MSE: 88.36692754990196
  * MAPE: inf
### Validate - platform - idle

  * expected:  `rate( kepler_node_platform_joules_total{ job="vm", mode="idle", }[20s] ) `
  * actual:  `rate( kepler_vm_platform_joules_total{ job="metal", vm_id=~".*my-vm", mode="idle", }[20s] ) `
#### Errors

  * MSE: 5676818830.251884
  * MAPE: 99.70747405272074
### Validate - package - idle

  * expected:  `rate( kepler_node_package_joules_total{ job="vm", mode="idle", }[20s] ) `
  * actual:  `rate( kepler_vm_package_joules_total{ job="metal", vm_id=~".*my-vm", mode="idle", }[20s] ) `
#### Errors

  * MSE: 4843.420398245913
  * MAPE: 21600.916902787263
### Validate - core - idle

  * expected:  `rate( kepler_node_core_joules_total{ job="vm", mode="idle", }[20s] ) `
  * actual:  `rate( kepler_vm_core_joules_total{ job="metal", vm_id=~".*my-vm", mode="idle", }[20s] ) `
#### Errors

  * MSE: 4846.721586292075
  * MAPE: 23324.601300622602
### Validate - dram - idle

  * expected:  `rate( kepler_node_dram_joules_total{ job="vm", mode="idle", }[20s] ) `
  * actual:  `rate( kepler_vm_dram_joules_total{ job="metal", vm_id=~".*my-vm", mode="idle", }[20s] ) `
#### Errors

  * MSE: 2218.9121977855402
  * MAPE: 128484.92135046214
