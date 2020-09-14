#!/usr/bin/env bash
# Author: Samuel Prevost <samuel.prevost@pm.me>
# Date  : 2020-08-30
# Licence: MIT Licence

if ! command -v rg 2>&1 > /dev/null; then
    echo "Please install ripgrep first !"
    exit 1
fi

unpaired=$(ls -1 $1 | sed -z '!d; s/pg\n/pg /g' | rg -v 'jpg.*json')
echo "Deleting the following: "
echo $unpaired

if [[ "$(read -e -p 'Continue? [y/N]> '; echo $REPLY)" == [Yy]* ]]; then
    rm $unpaired
fi

