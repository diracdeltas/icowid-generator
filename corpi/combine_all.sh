#!/usr/bin/env bash

cd "$(dirname "$0")"
rm *.txt
cat text/*.txt >> erowid.txt
cat ico_text/*.txt >> ico.txt
