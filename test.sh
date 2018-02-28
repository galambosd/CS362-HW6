#!/bin/bash


for i in $(seq $2)
do
	python3 make_genome.py $1 >/dev/null
	python3 simulate.py simple.fasta 25 150 .05 >/dev/null
	python3 assemble.py reads.txt 19 >/dev/null
	python3 test_assembly.py simple.fasta contigs.txt
done
exit 0
