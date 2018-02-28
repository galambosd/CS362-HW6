#!/bin/bash

# $@ will pass all parameters you passed to the shell script to the python script below
python3 assemble.py $@

dot -Tpng graph.dot -o DeBruijnGraph.png
