#!/usr/bin/env bash

# This is a script for converting ico-whitepapers PDF to text. In practice
# it does not give as good results as using MacOS Automator :(

OUTPUT=corpi/ico_text/ico.log

for f in `find ico-whitepapers -type f -name '*.pdf'`; do
    textract $f >> $OUTPUT
done
