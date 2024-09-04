# v0.7.11-196-g6a76bc35

## Build Info

   - `kepler_exporter_build_info{arch="amd64", branch="main", instance="localhost:8888", job="metal", os="linux", revision="6a76bc358e568575f8ceba94c8aef6aed26b013d", version="v0.7.11-196-g6a76bc35-dirty"}`
   - `kepler_exporter_build_info{arch="amd64", branch="main", instance="localhost:9999", job="vm", os="linux", revision="6a76bc358e568575f8ceba94c8aef6aed26b013d", version="v0.7.11-196-g6a76bc35-dirty"}`
## Node Info

   - `kepler_node_info{components_power_source="rapl-sysfs", cpu_architecture="Coffee Lake", instance="localhost:8888", job="metal", platform_power_source="acpi", source="os"}`
   - `kepler_node_info{components_power_source="estimator", cpu_architecture="Coffee Lake", instance="localhost:9999", job="vm", platform_power_source="none", source="os"}`
## Machine Specs

### Host

| Model | Sockets | Cores | Threads | Flags |
| --- | --- | --- | --- | --- |
| Intel(R) Xeon(R) E-2278G CPU @ 3.40GHz | 1 | 16 | 2 | `fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp vnmi md_clear flush_l1d arch_capabilities` |
### VM

| Model | Sockets | Cores | Threads | Flags |
| --- | --- | --- | --- | --- |
| Intel(R) Xeon(R) E-2278G CPU @ 3.40GHz | 10 | 10 | 1 | `fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon rep_good nopl xtopology cpuid tsc_known_freq pni pclmulqdq vmx ssse3 fma cx16 pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt xsaveopt xsavec xgetbv1 xsaves arat vnmi umip md_clear flush_l1d arch_capabilities` |
## Validation Results

   - Started At: `2024-09-04 02:17:36.070213`
   - Ended   At: `2024-09-04 02:34:23.586564`
   - Duration  : `0:16:47.516351`
## Validations

### Summary

| Name | MSE | MAPE | Pass / Fail |
| --- | --- | --- | --- |
| platform - absolute | 8156.91 | 411.03 | PASS |
| package - absolute | 14813.53 | 1225.32 | PASS |
| core - absolute | 14832.61 | 1254.05 | PASS |
| platform - dynamic | 915.99 | 209.58 | PASS |
| package - dynamic | 824.63 | 124.69 | PASS |
| core - dynamic | 822.27 | 124.73 | PASS |
| dram - dynamic | 0.23 | 6767.13 | PASS |
| platform - idle | 3810.53 | 3088.19 | PASS |
| package - idle | 20600.39 | 51454.22 | PASS |
| core - idle | 20612.29 | 60516.04 | PASS |
| dram - idle | 342.03 | 15210.92 | PASS |
### Details

#### platform - absolute


**Queries**:
   - Actual  : `sum( rate( kepler_vm_platform_joules_total{ job="metal", vm_id=~".*my-vm", }[20s] ) ) `
   - Expected: `sum( rate( kepler_node_platform_joules_total{ job="vm", }[20s] ) ) `

**Results**:
   - MSE  : `8156.91`
   - MAPE : `411.03 %`

**Charts**:
![platform - absolute](images/platform_absolute.png)
#### package - absolute


**Queries**:
   - Actual  : `sum( rate( kepler_vm_package_joules_total{ job="metal", vm_id=~".*my-vm", }[20s] ) ) `
   - Expected: `sum( rate( kepler_node_package_joules_total{ job="vm", }[20s] ) ) `

**Results**:
   - MSE  : `14813.53`
   - MAPE : `1225.32 %`

**Charts**:
![package - absolute](images/package_absolute.png)
#### core - absolute


**Queries**:
   - Actual  : `sum( rate( kepler_vm_core_joules_total{ job="metal", vm_id=~".*my-vm", }[20s] ) ) `
   - Expected: `sum( rate( kepler_node_core_joules_total{ job="vm", }[20s] ) ) `

**Results**:
   - MSE  : `14832.61`
   - MAPE : `1254.05 %`

**Charts**:
![core - absolute](images/core_absolute.png)
#### platform - dynamic


**Queries**:
   - Actual  : `rate( kepler_vm_platform_joules_total{ job="metal", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
   - Expected: `rate( kepler_node_platform_joules_total{ job="vm", mode="dynamic", }[20s] ) `

**Results**:
   - MSE  : `915.99`
   - MAPE : `209.58 %`

**Charts**:
![platform - dynamic](images/platform_dynamic.png)
#### package - dynamic


**Queries**:
   - Actual  : `rate( kepler_vm_package_joules_total{ job="metal", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
   - Expected: `rate( kepler_node_package_joules_total{ job="vm", mode="dynamic", }[20s] ) `

**Results**:
   - MSE  : `824.63`
   - MAPE : `124.69 %`

**Charts**:
![package - dynamic](images/package_dynamic.png)
#### core - dynamic


**Queries**:
   - Actual  : `rate( kepler_vm_core_joules_total{ job="metal", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
   - Expected: `rate( kepler_node_core_joules_total{ job="vm", mode="dynamic", }[20s] ) `

**Results**:
   - MSE  : `822.27`
   - MAPE : `124.73 %`

**Charts**:
![core - dynamic](images/core_dynamic.png)
#### dram - dynamic


**Queries**:
   - Actual  : `rate( kepler_vm_dram_joules_total{ job="metal", vm_id=~".*my-vm", mode="dynamic", }[20s] ) `
   - Expected: `rate( kepler_node_dram_joules_total{ job="vm", mode="dynamic", }[20s] ) `

**Results**:
   - MSE  : `0.23`
   - MAPE : `6767.13 %`

**Charts**:
![dram - dynamic](images/dram_dynamic.png)
#### platform - idle


**Queries**:
   - Actual  : `rate( kepler_vm_platform_joules_total{ job="metal", vm_id=~".*my-vm", mode="idle", }[20s] ) `
   - Expected: `rate( kepler_node_platform_joules_total{ job="vm", mode="idle", }[20s] ) `

**Results**:
   - MSE  : `3810.53`
   - MAPE : `3088.19 %`

**Charts**:
![platform - idle](images/platform_idle.png)
#### package - idle


**Queries**:
   - Actual  : `rate( kepler_vm_package_joules_total{ job="metal", vm_id=~".*my-vm", mode="idle", }[20s] ) `
   - Expected: `rate( kepler_node_package_joules_total{ job="vm", mode="idle", }[20s] ) `

**Results**:
   - MSE  : `20600.39`
   - MAPE : `51454.22 %`

**Charts**:
![package - idle](images/package_idle.png)
#### core - idle


**Queries**:
   - Actual  : `rate( kepler_vm_core_joules_total{ job="metal", vm_id=~".*my-vm", mode="idle", }[20s] ) `
   - Expected: `rate( kepler_node_core_joules_total{ job="vm", mode="idle", }[20s] ) `

**Results**:
   - MSE  : `20612.29`
   - MAPE : `60516.04 %`

**Charts**:
![core - idle](images/core_idle.png)
#### dram - idle


**Queries**:
   - Actual  : `rate( kepler_vm_dram_joules_total{ job="metal", vm_id=~".*my-vm", mode="idle", }[20s] ) `
   - Expected: `rate( kepler_node_dram_joules_total{ job="vm", mode="idle", }[20s] ) `

**Results**:
   - MSE  : `342.03`
   - MAPE : `15210.92 %`

**Charts**:
![dram - idle](images/dram_idle.png)
