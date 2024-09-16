# v0.7.11-227-g8a3587aa

## Build Info

   - `kepler_exporter_build_info{arch="amd64", branch="main", instance="kepler-metal:8888", job="metal", os="linux", revision="8a3587aa55e7dd2019d406a89443fba716352a7f", version="v0.7.11-227-g8a3587aa-dirty"}`
   - `kepler_exporter_build_info{arch="amd64", branch="main", instance="vm:9100", job="vm", os="linux", revision="8a3587aa55e7dd2019d406a89443fba716352a7f", version="v0.7.11-227-g8a3587aa-dirty"}`
## Node Info

   - `kepler_node_info{components_power_source="rapl-sysfs", cpu_architecture="Coffee Lake", instance="kepler-metal:8888", job="metal", platform_power_source="acpi", source="os"}`
   - `kepler_node_info{components_power_source="estimator", cpu_architecture="Coffee Lake", instance="vm:9100", job="vm", platform_power_source="none", source="os"}`
## Machine Specs

### Host

| Model | Sockets | Cores | Threads | Flags |
| --- | --- | --- | --- | --- |
| Intel(R) Xeon(R) E-2278G CPU @ 3.40GHz | 1 | 16 | 2 | `fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp md_clear flush_l1d arch_capabilities` |
### VM

| Model | Sockets | Cores | Threads | Flags |
| --- | --- | --- | --- | --- |
| Intel(R) Xeon(R) E-2278G CPU @ 3.40GHz | 14 | 14 | 1 | `fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon rep_good nopl xtopology cpuid tsc_known_freq pni pclmulqdq vmx ssse3 fma cx16 pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt xsaveopt xsavec xgetbv1 xsaves arat vnmi umip md_clear arch_capabilities` |
## Validation Results

   - Started At: `2024-09-16 11:48:17.923342`
   - Ended   At: `2024-09-16 12:05:08.219357`
   - Duration  : `0:16:50.296015`
## Validations

### Summary

| Name | MSE | MAPE | Pass / Fail |
| --- | --- | --- | --- |
| [node-rapl - kepler-package](#node-rapl---kepler-package) | 33.23 | 11.71 | PASS |
| [platform - absolute](#platform---absolute) | 4849.58 | 489.66 | PASS |
| [package - absolute](#package---absolute) | 24744.95 | 1107.90 | PASS |
| [core - absolute](#core---absolute) | 24769.26 | 1125.96 | PASS |
| [platform - dynamic](#platform---dynamic) | 648.28 | 172.44 | PASS |
| [package - dynamic](#package---dynamic) | 10694.93 | 489.55 | PASS |
| [core - dynamic](#core---dynamic) | 10706.86 | 491.21 | PASS |
| [dram - dynamic](#dram---dynamic) | 33.93 | nan | PASS |
| [cpu-time - absolute](#cpu-time---absolute) | 1846858.76 | 66.88 | PASS |
| [platform - idle](#platform---idle) | 3925.96 | 8562.04 | PASS |
| [package - idle](#package---idle) | 3514.68 | 190019.08 | PASS |
| [core - idle](#core---idle) | 3516.52 | 377861.23 | PASS |
| [dram - idle](#dram---idle) | 202.15 | 30290.04 | PASS |
### Details

#### node-rapl - kepler-package


**Queries**:
   - Actual  (node-rapl) : [`sum( rate( node_rapl_package_joules_total[20s] ) )`](artifacts/node-rapl-node_rapl_package_joules_total--absolute.json)
   - Predicted (kepler-package) : [`sum( rate( kepler_node_package_joules_total{ job="metal", }[20s] ) )`](artifacts/kepler-package-kepler_node_package_joules_total--absolute.json)

**Results**:
   - MSE  : `33.23`
   - MAPE : `11.71 %`

**Charts**:
![node-rapl - kepler-package](images/node-rapl-vs-kepler-package-node_rapl_kepler_package.png)
#### platform - absolute


**Queries**:
   - Actual  (metal) : [`sum( rate( kepler_vm_platform_joules_total{ job="metal", vm_id=~".*my-vm", }[20s] ) )`](artifacts/metal-kepler_vm_platform_joules_total--absolute.json)
   - Predicted (vm) : [`sum( rate( kepler_node_platform_joules_total{ job="vm", }[20s] ) )`](artifacts/vm-kepler_node_platform_joules_total--absolute.json)

**Results**:
   - MSE  : `4849.58`
   - MAPE : `489.66 %`

**Charts**:
![platform - absolute](images/metal-vs-vm-platform_absolute.png)
#### package - absolute


**Queries**:
   - Actual  (metal) : [`sum( rate( kepler_vm_package_joules_total{ job="metal", vm_id=~".*my-vm", }[20s] ) )`](artifacts/metal-kepler_vm_package_joules_total--absolute.json)
   - Predicted (vm) : [`sum( rate( kepler_node_package_joules_total{ job="vm", }[20s] ) )`](artifacts/vm-kepler_node_package_joules_total--absolute.json)

**Results**:
   - MSE  : `24744.95`
   - MAPE : `1107.90 %`

**Charts**:
![package - absolute](images/metal-vs-vm-package_absolute.png)
#### core - absolute


**Queries**:
   - Actual  (metal) : [`sum( rate( kepler_vm_core_joules_total{ job="metal", vm_id=~".*my-vm", }[20s] ) )`](artifacts/metal-kepler_vm_core_joules_total--absolute.json)
   - Predicted (vm) : [`sum( rate( kepler_node_core_joules_total{ job="vm", }[20s] ) )`](artifacts/vm-kepler_node_core_joules_total--absolute.json)

**Results**:
   - MSE  : `24769.26`
   - MAPE : `1125.96 %`

**Charts**:
![core - absolute](images/metal-vs-vm-core_absolute.png)
#### platform - dynamic


**Queries**:
   - Actual  (metal) : [`rate( kepler_vm_platform_joules_total{ job="metal", vm_id=~".*my-vm", mode="dynamic", }[20s] )`](artifacts/metal-kepler_vm_platform_joules_total--dynamic.json)
   - Predicted (vm) : [`rate( kepler_node_platform_joules_total{ job="vm", mode="dynamic", }[20s] )`](artifacts/vm-kepler_node_platform_joules_total--dynamic.json)

**Results**:
   - MSE  : `648.28`
   - MAPE : `172.44 %`

**Charts**:
![platform - dynamic](images/metal-vs-vm-platform_dynamic.png)
#### package - dynamic


**Queries**:
   - Actual  (metal) : [`rate( kepler_vm_package_joules_total{ job="metal", vm_id=~".*my-vm", mode="dynamic", }[20s] )`](artifacts/metal-kepler_vm_package_joules_total--dynamic.json)
   - Predicted (vm) : [`rate( kepler_node_package_joules_total{ job="vm", mode="dynamic", }[20s] )`](artifacts/vm-kepler_node_package_joules_total--dynamic.json)

**Results**:
   - MSE  : `10694.93`
   - MAPE : `489.55 %`

**Charts**:
![package - dynamic](images/metal-vs-vm-package_dynamic.png)
#### core - dynamic


**Queries**:
   - Actual  (metal) : [`rate( kepler_vm_core_joules_total{ job="metal", vm_id=~".*my-vm", mode="dynamic", }[20s] )`](artifacts/metal-kepler_vm_core_joules_total--dynamic.json)
   - Predicted (vm) : [`rate( kepler_node_core_joules_total{ job="vm", mode="dynamic", }[20s] )`](artifacts/vm-kepler_node_core_joules_total--dynamic.json)

**Results**:
   - MSE  : `10706.86`
   - MAPE : `491.21 %`

**Charts**:
![core - dynamic](images/metal-vs-vm-core_dynamic.png)
#### dram - dynamic


**Queries**:
   - Actual  (metal) : [`rate( kepler_vm_dram_joules_total{ job="metal", vm_id=~".*my-vm", mode="dynamic", }[20s] )`](artifacts/metal-kepler_vm_dram_joules_total--dynamic.json)
   - Predicted (vm) : [`rate( kepler_node_dram_joules_total{ job="vm", mode="dynamic", }[20s] )`](artifacts/vm-kepler_node_dram_joules_total--dynamic.json)

**Results**:
   - MSE  : `33.93`
   - MAPE : `nan %`

**Charts**:
![dram - dynamic](images/metal-vs-vm-dram_dynamic.png)
#### cpu-time - absolute


**Queries**:
   - Actual  (metal) : [`sum( rate( kepler_vm_bpf_cpu_time_ms_total{ vm_id=~".*my-vm", job="metal" }[20s] ) )`](artifacts/metal-kepler_vm_bpf_cpu_time_ms_total--absolute.json)
   - Predicted (vm) : [`sum( rate( kepler_process_bpf_cpu_time_ms_total{ job="vm", }[20s] ) )`](artifacts/vm-kepler_process_bpf_cpu_time_ms_total--absolute.json)

**Results**:
   - MSE  : `1846858.76`
   - MAPE : `66.88 %`

**Charts**:
![cpu-time - absolute](images/metal-vs-vm-cpu_time_absolute.png)
#### platform - idle


**Queries**:
   - Actual  (metal) : [`rate( kepler_vm_platform_joules_total{ job="metal", vm_id=~".*my-vm", mode="idle", }[20s] )`](artifacts/metal-kepler_vm_platform_joules_total--idle.json)
   - Predicted (vm) : [`rate( kepler_node_platform_joules_total{ job="vm", mode="idle", }[20s] )`](artifacts/vm-kepler_node_platform_joules_total--idle.json)

**Results**:
   - MSE  : `3925.96`
   - MAPE : `8562.04 %`

**Charts**:
![platform - idle](images/metal-vs-vm-platform_idle.png)
#### package - idle


**Queries**:
   - Actual  (metal) : [`rate( kepler_vm_package_joules_total{ job="metal", vm_id=~".*my-vm", mode="idle", }[20s] )`](artifacts/metal-kepler_vm_package_joules_total--idle.json)
   - Predicted (vm) : [`rate( kepler_node_package_joules_total{ job="vm", mode="idle", }[20s] )`](artifacts/vm-kepler_node_package_joules_total--idle.json)

**Results**:
   - MSE  : `3514.68`
   - MAPE : `190019.08 %`

**Charts**:
![package - idle](images/metal-vs-vm-package_idle.png)
#### core - idle


**Queries**:
   - Actual  (metal) : [`rate( kepler_vm_core_joules_total{ job="metal", vm_id=~".*my-vm", mode="idle", }[20s] )`](artifacts/metal-kepler_vm_core_joules_total--idle.json)
   - Predicted (vm) : [`rate( kepler_node_core_joules_total{ job="vm", mode="idle", }[20s] )`](artifacts/vm-kepler_node_core_joules_total--idle.json)

**Results**:
   - MSE  : `3516.52`
   - MAPE : `377861.23 %`

**Charts**:
![core - idle](images/metal-vs-vm-core_idle.png)
#### dram - idle


**Queries**:
   - Actual  (metal) : [`rate( kepler_vm_dram_joules_total{ job="metal", vm_id=~".*my-vm", mode="idle", }[20s] )`](artifacts/metal-kepler_vm_dram_joules_total--idle.json)
   - Predicted (vm) : [`rate( kepler_node_dram_joules_total{ job="vm", mode="idle", }[20s] )`](artifacts/vm-kepler_node_dram_joules_total--idle.json)

**Results**:
   - MSE  : `202.15`
   - MAPE : `30290.04 %`

**Charts**:
![dram - idle](images/metal-vs-vm-dram_idle.png)
