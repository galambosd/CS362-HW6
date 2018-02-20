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


print(sys.argv)

with open("reads.txt","w") as output:
    for arg in sys.argv:
        output.write("\n")
        output.write(arg)
    output.close()

#'parse' the FASTA file by just skipping the 1st line
fasta.readline()
fastaSeq = fasta.read().rstrip('\n')
fasta.close()

# calculate N using G (length of FASTA), C (coverage), L (length of the reads)
# if it's not an int, round up

# N times...
    # choose a random index from the FASTA
    # splice something of length L
    # add the read to our set of reads

    #later...
        # handle the edge case indices accordingly
        # introduce the necessary frequency of errors before storing the read

# output all of our reads into reads.txt
