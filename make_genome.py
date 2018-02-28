from sys import argv
from random import randint

length = argv[1]

nucleotides = ['A', 'C', 'T', 'G']

genome = ''
for i in range(0, length):
    genome+= nucleotides[randint(0,3)]

with open('simple.fasta', 'w') as outFile:
    outFile.write('>Genome generated with make_genome.py\n')
    outFile.write(genome+'\n')
    outFile.close()

print('Done.')
