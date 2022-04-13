#!/bin/bash
: > output.csv # flush results
find output -type f -delete # flush output
./sort-all.py