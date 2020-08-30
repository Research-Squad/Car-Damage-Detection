#!/usr/bin/env bash
# Author: Samuel Prevost <samuel.prevost@pm.me>
# Date  : 2020-08-30
# Licence: MIT Licence

if ! command -v jq 2>&1 > /dev/null; then
    echo "Please install jq first !"
    exit 1
fi

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 file1.json file2.json ..."
    exit 1
fi

jq '.shapes[].label' -r $@ | sort | uniq -c | sort -V
