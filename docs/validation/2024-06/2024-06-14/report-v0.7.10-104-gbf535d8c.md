# v0.7.10-104-gbf535d8c
## Specs
### Host CPU Specs
| Model | Cores | Threads | Sockets | Flags |
|-----------|-----------|-------------|-------------|-----------|
| Intel(R) Xeon(R) E-2278G CPU @ 3.40GHz | 16 | 2 | 1 | ```fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb invpcid_single ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt intel_pt xsaveopt xsavec xgetbv1 xsaves dtherm ida arat pln pts hwp hwp_notify hwp_act_window hwp_epp vnmi md_clear flush_l1d arch_capabilities``` |
### VM CPU Specs
| Model | Cores | Threads | Sockets | Flags |
|-----------|-----------|-------------|-------------|-----------|
| Intel(R) Xeon(R) E-2278G CPU @ 3.40GHz | 4 | 1 | 4 | ```fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon rep_good nopl xtopology cpuid tsc_known_freq pni pclmulqdq vmx ssse3 fma cx16 pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm 3dnowprefetch cpuid_fault ssbd ibrs ibpb stibp ibrs_enhanced tpr_shadow flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid mpx rdseed adx smap clflushopt xsaveopt xsavec xgetbv1 xsaves arat vnmi umip md_clear flush_l1d arch_capabilities``` |
### Host DRAM Size
| Size |
|------|
| 32750376 kB |
### VM DRAM Size
| Size |
|------|
| 16114604 kB |

## Validation Results
#### Query
```avg_over_time((( rate(kepler_vm_core_joules_total{vm_id=~'.*my-vm', mode='dynamic', job='node'}[300s]) - on() rate(kepler_node_core_joules_total{job='vm', mode='dynamic'}[300s]) )^2 )[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time(((rate(kepler_vm_dram_joules_total{vm_id=~'.*my-vm', mode='dynamic', job='node'}[300s]) - on() rate(kepler_node_dram_joules_total{job='vm', mode='dynamic'}[300s]))^2)[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time(((rate(kepler_vm_package_joules_total{vm_id=~'.*my-vm', mode='dynamic', job='node'}[300s]) - on() rate(kepler_node_package_joules_total{job='vm', mode='dynamic'}[300s]))^2 )[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time(((rate(kepler_vm_platform_joules_total{vm_id=~'.*my-vm', mode='dynamic', job='node'}[300s]) - on() rate(kepler_node_platform_joules_total{job='vm', mode='dynamic'}[300s]))^2)[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time(((rate(kepler_vm_core_joules_total{vm_id=~'.*my-vm', mode='idle', job='node'}[300s]) - on() rate(kepler_node_core_joules_total{job='vm', mode='idle'}[300s]))^2)[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time(((rate(kepler_vm_dram_joules_total{vm_id=~'.*my-vm', mode='idle', job='node'}[300s]) - on() rate(kepler_node_dram_joules_total{job='vm', mode='idle'}[300s]))^2)[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time(((rate(kepler_vm_package_joules_total{vm_id=~'.*my-vm', mode='idle', job='node'}[300s]) - on() rate(kepler_node_package_joules_total{job='vm', mode='idle'}[300s]))^2)[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time(((rate(kepler_vm_platform_joules_total{vm_id=~'.*my-vm', mode='idle', job='node'}[300s]) - on() rate(kepler_node_platform_joules_total{job='vm', mode='idle'}[300s]))^2) [300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time((abs(rate(kepler_vm_core_joules_total{vm_id=~'.*my-vm', mode='dynamic', job='node'}[300s]) - on() rate(kepler_node_core_joules_total{job='vm', mode='dynamic'}[300s])) / on() rate(kepler_vm_core_joules_total{vm_id=~'.*my-vm', mode='dynamic', job='node'}[300s]))[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time((abs(rate(kepler_vm_dram_joules_total{vm_id=~'.*my-vm', mode='dynamic', job='node'}[300s]) - on() rate(kepler_node_dram_joules_total{job='vm', mode='dynamic'}[300s])) / on() rate(kepler_vm_dram_joules_total{vm_id=~'.*my-vm', mode='dynamic', job='node'}[300s]))[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time((abs(rate(kepler_vm_package_joules_total{vm_id=~'.*my-vm', mode='dynamic', job='node'}[300s]) - on() rate(kepler_node_package_joules_total{job='vm', mode='dynamic'}[300s])) / on() rate(kepler_vm_package_joules_total{vm_id=~'.*my-vm', mode='dynamic', job='node'}[300s]))[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time((abs(rate(kepler_vm_platform_joules_total{vm_id=~'.*my-vm', mode='dynamic', job='node'}[300s]) - on() rate(kepler_node_platform_joules_total{job='vm', mode='dynamic'}[300s])) / on() rate(kepler_vm_platform_joules_total{vm_id=~'.*my-vm', mode='dynamic', job='node'}[300s]))[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time((abs(rate(kepler_vm_core_joules_total{vm_id=~'.*my-vm', mode='idle', job='node'}[300s]) - on() rate(kepler_node_core_joules_total{job='vm', mode='idle'}[300s])) / on() rate(kepler_vm_core_joules_total{vm_id=~'.*my-vm', mode='idle', job='node'}[300s]))[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time((abs(rate(kepler_vm_dram_joules_total{vm_id=~'.*my-vm', mode='idle', job='node'}[300s]) - on() rate(kepler_node_dram_joules_total{job='vm', mode='idle'}[300s])) / on() rate(kepler_vm_dram_joules_total{vm_id=~'.*my-vm', mode='idle', job='node'}[300s]))[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time((abs(rate(kepler_vm_package_joules_total{vm_id=~'.*my-vm', mode='idle', job='node'}[300s]) - on() rate(kepler_node_package_joules_total{job='vm', mode='idle'}[300s])) / on() rate(kepler_vm_package_joules_total{vm_id=~'.*my-vm', mode='idle', job='node'}[300s]))[300s:])```
#### Average Error
0
#### Error List
[]

#### Query
```avg_over_time((abs(rate(kepler_vm_platform_joules_total{vm_id=~'.*my-vm', mode='idle', job='node'}[300s]) - on() rate(kepler_node_platform_joules_total{job='vm', mode='idle'}[300s])) / on() rate(kepler_vm_platform_joules_total{vm_id=~'.*my-vm', mode='idle', job='node'}[300s]))[300s:])```
#### Average Error
0
#### Error List
[]

