#!/bin/bash
set -e

# Create the directory for cloud-init files
mkdir -p /var/lib/cloud/seed/nocloud-net

# Copy the user-data and meta-data files to the directory
cp /tmp/user-data /var/lib/cloud/seed/nocloud-net/user-data
cp /tmp/meta-data /var/lib/cloud/seed/nocloud-net/meta-data