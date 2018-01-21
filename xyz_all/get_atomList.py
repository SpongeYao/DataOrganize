import sys

inputFile= sys.argv[1]
outputFile= sys.argv[2]

f = open(inputFile,"r")
out= open(outputFile, 'w')
index=0
for line in f:
    index= index+1
    if index<=2:
        continue 
    atom= line.strip().split(' ')[0]
    print '{1} Atom: {0}'.format(atom, index)
    out.write(atom+'\n')

out.close()
