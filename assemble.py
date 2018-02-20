import sys

try:
    reads = open(sys.argv[1]."r")
    k = int(sys.argv[2])
except(IndexError):
    print("Too few arguments found. Assemble requires a txt reads file and a k-mer length.")
    exit(1)
except(FileNotFoundError):
    print("Text file not found. Try again.")
    exit(1)
except(ValueError):
    print("K-mer length must be an integer.")
    exit(1)




with open("contigs.txt","w") as output:
    for arg in sys.argv:
        output.write("\n")
        output.write(arg)
    output.close()
