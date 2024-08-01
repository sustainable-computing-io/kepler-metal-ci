#!/usr/bin/awk -f

# Function to calculate mean, standard deviation, min, and max
function stats(values, n, result) {
    sum = 0
    min = values[1]
    max = values[1]
    for (i = 1; i <= n; i++) {
        sum += values[i]
        if (values[i] < min) min = values[i]
        if (values[i] > max) max = values[i]
    }
    mean = sum / n

    sum = 0
    for (i = 1; i <= n; i++) {
        sum += (values[i] - mean) * (values[i] - mean)
    }
    variance = sum / (n - 1)
    stddev = sqrt(variance)

    result["mean"] = mean
    result["stddev"] = stddev
    result["min"] = min
    result["max"] = max
}

BEGIN {
    FS = "[:,%]";
    n = 0
}

{
    # The input is Time: 2024-06-13 00:27:08, Utilization: 0.015371240409722223%
    utilization[++n] = $6
}

END {
    if (n == 0) {
        print "| N/A | N/A |"
        exit
    }
    stats(utilization, n, result)
    printf "| %.10f%% | %.10f%% |", result["mean"], result["stddev"]
}
