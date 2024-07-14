#!/bin/bash
# Prometheus server URL
set -x
PROMETHEUS_URL="http://localhost:9090/api/v1/query"

# Prometheus query
QUERY="kepler_node_package_joules_total"

# Function to query Prometheus and check for values
query_prometheus() {
    RESPONSE=$(curl -sG --data-urlencode "query=$QUERY" $PROMETHEUS_URL)
    VALUES=$(echo $RESPONSE | jq '.data.result | length')
    echo $VALUES
}

# Retry 20 times with 5 seconds interval
for i in {1..20}; do
VALUES=$(query_prometheus)
if [ "$VALUES" -gt 0 ]; then
    echo "Values found in the query result."
    exit 0
else
    echo "No values found yet, retrying in 5 seconds..."
    sleep 5
fi
done

echo "Debugging"

kubectl get po --all-namespaces

echo "Exiting"
#exit 1