#!/usr/bin/env bash

cd "$(dirname "$0")"
export LANG=C

rm *.txt
cat text/*.txt | tr -cd '\11\12\15\40-\176' >> erowid.txt
node process_json.js
