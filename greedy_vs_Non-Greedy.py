import re

fname = input("Enter the File name:")
lines = open(fname)

for line in lines:
    line = line.rstrip()
#this is an give the output as greedy (i.e Largest One)
#    line = re.findall("^F.+:",line)
#    print(line)

#Now fixing the greedy (by the use of ?) => Which will now become Non-Greedy(Smallest)
    line=re.findall("^F.+?:",line)
    print(line)