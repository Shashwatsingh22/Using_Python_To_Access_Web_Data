import re
fname = input("Enter The File Name:")
lines=open(fname)

for line in lines:
    line=line.rstrip()
    line=re.findall("[0-9]+",line)
    print(line)