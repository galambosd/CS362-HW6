from sys import argv

file1 = argv[1]
file2 = argv[2]

data = []
for file in argv[1:]:
    with open(file,'r') as original:
        if '.fasta' in file:
            
            original.readline()
        originalSeq = original.read()
        original.close()
        data.append(originalSeq.replace("\n","").upper())



print(data[0] == data[1])
