# Kepler Metal CI

Running Kepler on Equinix and AWS Metal instances with GitHub Actions

## Equinix Metal Runner

[This action](.github/workflows/equinix_metal_flow.yml) is used to demo how to deploy a GitHub self hosted runner on Equinix Metal, run some workload, and delete the runner.

### Setup

- Create GitHub personal access token following [this instruction](https://docs.github.com/en/rest/actions/self-hosted-runners?apiVersion=2022-11-28#create-configuration-for-a-just-in-time-runner-for-an-organization)
- Create a project with the [Equinix Metal Project Action](https://github.com/equinix-labs/metal-runner-action) to create the self hosted runner
- Run some workload
- Delete the runner with the [Equinix Metal Sweeper Action](https://github.com/sustainable-computing-io/metal-sweeper-action). Note, this action only deletes the server that serves the self hosted runner. It doesn't sweep other servers as the Equinix Metal Sweeper does.

### Importing Prometheus Snapshot data from Validation Runs

To import the Prometheus data from the validation runs, follow these steps:

- Navigate to the directory containing the snapshot tar file, typically found in:

```bash
docs/validation/<date>/<validator_dir>/prometheus-snapshot
```

Extract the tar file.

- Ensure you have a local Prometheus instance set up. Identify the location of its data directory
- Copy the extracted snapshot contents into Prometheus data directory

```bash
cp -r <snapshot_directory>/* <prometheus_data_directory>
```

### Workflows

- Validation with Standalone Kepler: Deploys Kepler on baremetal and virtual machine on Equinix. Validates the energy prediction of Kepler on virtual machine.
- Validation with Model Server: Deploys Kepler on baremetal and Kepler with Kepler Model Server on virtual machine on Equinix. Validates the energy prediction of Kepler with Model Server on Virtual Machine.
- Training and Validation e2e with Single Server: Provisions Equinix Server, Trains Models locally on server, Validates trained models with Model Server on Virtual Machine.
- Training and Validation e2e with Isolated Servers: Provisions Equinix Server, Trains Models locally on Server, Provisions a separate Equinix Server, Validates trained models with Model Server on Virtual Machine on new Server
