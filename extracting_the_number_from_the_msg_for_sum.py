import re

fname = input("Enter the File name: ")
lines = open(fname)
numlist = list()
summ=0
count=0

for line in lines:
    line = line.rstrip()
    li = re.findall("[0-9]+",line)
    numlist.extend(li)
for i in numlist:
    summ=summ+int(i)
    count=count+1    
print(summ,count)