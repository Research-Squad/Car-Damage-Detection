#!/usr/bin/env bash
# Author: Samuel Prevost <samuel.prevost@pm.me>
# Date  : 2020-08-30
# Licence: MIT Licence

if ! command -v fdfind 2>&1 > /dev/null && ! command -v fd 2>&1 > /dev/null; then
    echo "Please install fdfind first !"
    exit 1
fi

if command -v fdfind 2>&1 > /dev/null; then
    FD_CMD=fdfind
elif command -v fd 2>&1 > /dev/null; then
    FD_CMD=fd
fi

if [ "$#" -ge 1 ]; then
    all_valid=true
    for argpath in $@; do
        if [ ! -d $argpath ]; then
            echo "$argpath is not a valid directory"
            all_valid=false
            break
        fi
    done
    if ! $all_valid; then
        echo "Usage: $0 [search_folder1 search_folder2 ...]"
        echo "Recursively lists absolute paths to every matching .json and .jpg files contained in the provided search folders (and their subfolders etc..)."
        echo -e "\nWithout argument, the current directory is used as the search folder"
        exit 1
    fi
fi

if [ "$#" -lt 1 ]; then
    SEARCH_PATH=$PWD
else
    SEARCH_PATH="$@"
fi

echo "Search path is $SEARCH_PATH" >&2

trap "rm filepaths.txt filenames_and_paths.csv filenames_and_paths_uniq.csv filenames_and_paths_matching.csv" EXIT

# Lists all paths to json and jpeg files which start with dates in their filename
$FD_CMD -j $(nproc) --absolute-path -e json -e jpg '^\d{4}-\d{2}-\d{2}' $@ > filepaths.txt
# Prepend the filename to each line
sed -E -e '!d; s/^(.*\/)(.*)$/\2,\1\2/g' filepaths.txt > filenames_and_paths.csv
# Sort and uniq every line based on the filename
sort -u -t, -k 1,1 filenames_and_paths.csv -o filenames_and_paths_uniq.csv
# Keeps all lines that contain "json" and also the line right before it
# since jpg>json in lexicographic order, the file right before is garanteed
# to be a jpg file of the same name
rg 'json' -B 1 --no-context-separator filenames_and_paths_uniq.csv > filenames_and_paths_matching.csv
cut -d ',' -f 2 filenames_and_paths_matching.csv > matching.txt

line_count=$(cat matching.txt | wc -l)
pair_count=$((line_count/2))
echo "Done. $pair_count jpeg/json pairs found."
echo "Outputted to matching.txt"
