#!/bin/bash

# Function to check the status of pipelineruns
check_pipelineruns() {
    statuses=$(kubectl get pipelineruns -o jsonpath='{range .items[*]}{.metadata.name} {.status.conditions[*].status} {.status.conditions[*].reason}{"\n"}{end}')

    all_completed=true

    while read -r name status reason; do
        if [[ "$status" == "Unknown" && "$reason" == "Running" ]]; then
            all_completed=false
            break
        fi
    done <<< "$statuses"

    echo $all_completed
}

while true; do
    if [ "$(check_pipelineruns)" == "true" ]; then
        echo "All PipelineRuns have completed."
        break
    else
        echo "Waiting for PipelineRuns to complete..."
        sleep 10 
    fi
done
