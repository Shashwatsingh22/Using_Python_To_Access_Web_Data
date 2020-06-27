import re
fname = input("Enter the File Name:")
lines = open(fname)

for line in lines:
    line = line.rstrip()
    line = re.findall("\S+@\S+",line)
    print(line)