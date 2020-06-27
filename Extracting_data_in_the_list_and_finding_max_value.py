#Extracting Data In the list and then finding the max in it...
import re
fname = input("Enter the File Name: ")
lines = open(fname)
numlist = list()

for line in lines:
    line = line.rstrip()
    stuf=re.findall("[0-9. ]+",line)
    print(stuf)
    if len(stuf)!=1 :continue
    num=int(stuf[0])
    numlist.append(num)
print("Maximum is: ",max(numlist))

