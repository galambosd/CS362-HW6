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
# throw out any that're too short

usable = []
for read in reads:
    if k <= len(read):
        usable.append(read)

if usable == []:
    print("You tried to create k-mers that are longer than your reads.")
    exit(1)
    
# build set of all k-mers
kMers = []
for read in reads:
    for i in range(0, len(read)-k+1):
        kMers.append(read[i:i+k])

#print(kMers)
# build (k-1)mers?
# create a class for our DB Graph?
totalConnections = 0
graph = {}
for kMer in kMers:
    totalConnections += 1
    k1Mer = kMer[:-1]
    k2Mer = kMer[1:]
    if k1Mer in graph.keys():
        if k2Mer in graph[k1Mer].keys():
            graph[k1Mer][k2Mer] += 1
        else:
            graph[k1Mer][k2Mer] = 1
    else:
        graph[k1Mer] = {k2Mer:1}
    if k2Mer not in graph.keys():
        graph[k2Mer] = {}


print("graph complete")

beginnings = []


for key in graph:
    
    isalone = True
    for kmer in graph:
        if key in graph[kmer]:
            isalone = False
            break
    if isalone:
        beginnings.append(key)
        print(len(beginnings))





numConnects = -1
for start in beginnings:
    curConnects = 0
    for key in graph[start]:
        curConnects += graph[start][key]
    if curConnects > numConnects:
        numConnects = curConnects
        beginning = start



#We're gonna visualize this with dot now.
if len(graph)<50:
    print("Doing dot stuff")
    with open("graph.dot","w") as dotFile:
        dotFile.write("digraph DeBruijn{\n")
        for key in graph.keys():
            for kmer in graph[key].keys():
                for i in range(0,graph[key][kmer]):
                    dotFile.write("\t\"" + key + "\"->\"" + kmer + "\"\n")
        dotFile.write("}")
        dotFile.close()
else:
    print("avoiding the dot file because it's probably scary")
print("found the greedy start.")
current = beginning
rstring = beginning
totalConnects = 0
numNodes = 0
inLoop = False
while len(graph[current]) != 0:
    
    numConnects = -1
    for kmer in graph[current]:
        if graph[current][kmer] > numConnects:
            nxt = kmer
            numConnects = graph[current][kmer]
    if numNodes > 3:
        graph[current][nxt] -= totalConnects//numNodes
    if numNodes > k and totalConnects/numNodes * 1.6 < numConnects:
        if not inLoop:
            print("predicting loop at " , current)
            print("avg: ", totalConnects/numNodes)
            print("connections: ", numConnects)
        inLoop = True
        
    else:
        if inLoop:
            print("we've exited a loop/are taking a loop. Hopefully we chose right.")
            print(current)
            print(nxt)
            inLoop = False
        numNodes += 1
        totalConnects += numConnects
    current = nxt
    rstring += nxt[-1:]

    

with open("contigs.txt","w") as rFile:
    rFile.write(rstring)
    rFile.close()



