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
json_files=$($FD_CMD -j $(nproc) --absolute-path '^\d{4}-\d{2}-\d{2}.*.json$' $SEARCH_PATH)

counter=0
while read -r json_filepath; do
    filename=$(basename "$json_filepath")
    image_filename=${filename%.*}.jpg
    image_filepath=$($FD_CMD -j $(nproc) --absolute-path -F "$image_filename" $SEARCH_PATH | head -n 1);
    if [ -n "$image_filepath" ]; then
        echo $json_filepath;
        echo $image_filepath;
        count=$((count+1))
        echo -ne "Found $count annotated images\r" >&2
    fi
done <<< "$json_files"
echo -e "\nAll $# subdir explored" >&2
