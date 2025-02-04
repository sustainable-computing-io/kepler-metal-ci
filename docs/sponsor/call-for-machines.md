# Call for Machines

## Expected Usage

- Periodic report: run training and validation workflow once per week and each run can spend upto 1 hour depends on the machine processing speed.
  The frequency and period of running could be changed with notice and will be applied only with approval.

- Release execution: run training, validation, and export workflow on each Kepler release.

## Type of Machines

As mentioned in several research works, the power consumption behavior can be varied by several factors.
Using the right power model to predict power consumption on the machine that has no power meter is critical the precision of the reported values.

We are seeking machines with the following characteristics, commonly used in cloud computing environments but not limited to:

### Processor
- Intel: Cascade Lake, Skylake (or newer)
- Ampere: Altra, AmpereOne (or newer)
- AMD: Opteron, EPYC (or newer)

### Accelerator Chips

- NVML-supported GPU

    |Architecture|Microarchitecture|Supported GPUs|
    |---|---|---|
    |Kepler|GK104, GK106, GK107|GeForce GTX 600 series (e.g., GTX 660, GTX 670), GTX 700 series|
    |Maxwell|GM204, GM206|GeForce GTX 900 series (e.g., GTX 970, GTX 980)|
    |Pascal|GP100, GP102|GeForce GTX 10 series (e.g., GTX 1080, GTX 1070), Titan X|
    |Volta|GV100|Tesla V100, Titan V|
    |Turing|TU102, TU104|GeForce RTX 20 series (e.g., RTX 2080 Ti, RTX 2070)|
    |Ampere|GA100|A100, A40, RTX 30 series (e.g., RTX 3090)|
    |Ada Lovelace|AD102|RTX 40 series (e.g., RTX 4090)|
    |Hopper|GH100|H100|


- DCGM-supported GPU

    |Architecture|Supported GPUs|
    |---|---|
    |Kepler|Tesla K80 and newer|
    |Maxwell|Tesla M10, Tesla M60|
    |Pascal|Tesla P100, Tesla P40, Tesla P4|
    |Volta|Tesla V100|
    |Turing|T4, Quadro RTX 4000, RTX A4000|
    |Ampere|A100, A40, A30, A10, A2, RTX A6000, RTX A5000|
    |Hopper|H100, H200|

- HLML-supported Intel Gaudi

> Please note that power source modules for other accelerator cards, such as AMD GPUs, Google TPUs, and IBM AIUs, are not yet supported by Kepler.
> Contributions to support these devices are always welcome within the Kepler community.

### Power meters
- rapl
- powerclamp
- amd-pstate
- acpi
- hmc
- redfish
- nvml (nvidia)
- hlml (habana)
- dcgm

### Available machines on CI

List of currently available bare metal machines for power model training and validation CI pipeline in [kepler-metal-ci](https://github.com/sustainable-computing-io/kepler-metal-ci/tree/main).

|processor|cores|chips|memory|power meters|source|sponsor|key contact
|---|---|---|----|---|---|---|---|
|intel_xeon_e_2278g| 16 | 1 | - | RAPL (package, core, dram)|equinix c3.small.x86|CNCF|@rootfs|
|intel_xeon_platinum_8259cl| 96 | 2 | 377| RAPL (package, dram)|ec2 m5.metal|RedHat|@rootfs|
|intel_xeon_e5_2686v4| 72 | 2 | 503| RAPL (package, dram)|ec2 i3.metal|RedHat|@rootfs|
|intel_xeon_platinum_8275cl| 96 | 2 | 188| RAPL (package, dram)|ec2 c5.metal|RedHat|@rootfs|
|intel_xeon_platinum_8259cl| 96 | 2 | 755| RAPL (package, dram)|ec2 r5.metal|RedHat|@rootfs|
|intel_xeon_platinum_8252c| 48 | 2 | 188 | RAPL (package, dram)|ec2 m5zn.metal|RedHat|@rootfs|
|intel_xeon_platinum_8488c| 96 | 1 | 377 | RAPL (package, dram)|ec2 m7i.metal-24xl|RedHat|@rootfs|
