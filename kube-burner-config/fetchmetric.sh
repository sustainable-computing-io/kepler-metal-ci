#!/usr/bin/env bash
#
# This file is part of the Kepler project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Copyright 2023 The Kepler Contributors
#
# shellcheck disable=SC1091
curl -G 'http://localhost:9090/api/v1/query_range' \
            --data-urlencode "query=$1" \
            --data-urlencode "start=${START_TIME}" --data-urlencode "end=${END_TIME}" --data-urlencode "step=5" \
            | jq -r '.data.result[0].values[] | @tsv' | awk '{printf "Time: %s, Utilization: %s%%\n", strftime("%Y-%m-%d %H:%M:%S", $1), $2}' \
            | tee $2 || true