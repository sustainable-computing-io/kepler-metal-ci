#!/bin/bash

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
        echo "trainer pipelineruns are complete."
        break
    else
        echo "waiting for trainer pipelineRuns to complete..."
        sleep 60 
    fi
done
