# CI playground
Testing different CI and Github Action pipelines before adding to Kepler main repos.

# Equinix Metal Runner
[This action](.github/workflows/equinix_metal_flow.yml) is used to demo how to deploy a GitHub self hosted runner on Equinix Metal, run some workload, and delete the runner.

## Setup

- Create GitHub personal access token following [this instruction](https://docs.github.com/en/rest/actions/self-hosted-runners?apiVersion=2022-11-28#create-configuration-for-a-just-in-time-runner-for-an-organization)
- Create a project with the [Equinix Metal Project Action](https://github.com/equinix-labs/metal-runner-action) to create the self hosted runner
- Run some workload
- Delete the runner with the [Equinix Metal Delete Action](https://github.com/rootfs/metal-delete-action). Note, this action only deletes the server that serves the self hosted runner. It doesn't sweep other servers as the Equinix Metal Sweeper does.