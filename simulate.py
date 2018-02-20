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
    



