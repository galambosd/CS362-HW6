import sys

try:
    readFile = open(sys.argv[1],"r")
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

reads = []
# read in the reads
for line in readFile.readlines():
    reads.append(line.rstrip('\n').upper())
# check that k isn't longer than reads
# assuming all reads same length
if k > len(reads[0]):
    print("You tried to create k-mers that are longer than your reads.")
    exit(1)
# build set of all k-mers
kMers = []
for read in reads:
    for i in range(0, len(read)-k+1):
        kMers.append(read[i:i+k])

# build (k-1)mers?
# create a class for our DB Graph?

graph = {}
for kMer in kMers:
    k1Mer = kMer[:-1]
    k2Mer = kMer[1:]
    if k1Mer in graph.keys():
        graph[k1Mer].append(k2Mer)
    else:
        graph[k1Mer] = [k2Mer]
    if k2Mer not in graph.keys():
        graph[k2Mer] = []
        
#We're gonna visualize this with dot now.


with open("graph.dot","w") as dotFile:
    dotFile.write("digraph DeBruijn{\n")
    for key in graph.keys():
        for value in graph[key]:
            dotFile.write("\t\"" + key + "\"->\"" + value + "\"\n")
    dotFile.write("}")
    dotFile.close()

        

with open("contigs.txt","w") as output:
    for arg in sys.argv:
        output.write("\n")
        output.write(arg)
    output.close()
