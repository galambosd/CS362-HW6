import sys


try:
    fasta = open(sys.argv[1],"r")
    coverage = int(sys.argv[2])
    readLength = int(sys.argv[3])
    errorRate = float(sys.argv[4])
    assert(errorRate < 1 and errorRate >= 0)
except(IndexError):
    print("""Too few arguments found.
          This file takes in a fasta file, a coverage value,
          a read length, and an error rate.""")
    exit(1)
except(ValueError):
    print("Coverage and read length must be integers. Error rate must be a float.")
    exit(1)
except(FileNotFoundError):
    print("FASTA file not found. Try again.")
    exit(1)
except(AssertionError):
    print("Error rate must be between 0 and 1. You gave a value of ", errorRate)
    exit(1)




from random import randint
from random import random
#'parse' the FASTA file by just skipping the 1st line
fasta.readline()
fastaSeq = fasta.read()
fasta.close()
fastaSeq = fastaSeq.replace("\n","").upper()

print(fastaSeq)

if len(fastaSeq) < readLength:
    print("you want a read length greater than the sequence given.")
    exit(1)

# calculate N using G (length of FASTA), C (coverage), L (length of the reads)
N = len(fastaSeq) * coverage // readLength
# if it's not an int, round up

# N times...
reads = []
for i in range(0,N):
    # choose a random index from the FASTA
    start = randint(-readLength,len(fastaSeq)-1)
    
    read = ""
    # splice something of length L
    
    end = min(start + readLength,len(fastaSeq))
    if start < 0:
        start = 0
    for ch in fastaSeq[start:end]:
        if random() < errorRate:
            # add an error at a corresponding rate to the error rate
            nucleotides = ["A","T","C","G"]
            nucleotides.remove(ch)
            # chooses a random other nucleotide
            read += nucleotides[randint(0,2)]
        else:
            read += ch
    # add the read to our set of reads
    reads.append(read)

    
    
    

    #later...
        # handle the edge case indices better
        # introduce the necessary frequency of errors before storing the read

# output all of our reads into reads.txt
with open("reads.txt","w") as output:
    for read in reads:
        
        output.write(read)
        output.write("\n")
    output.close()
