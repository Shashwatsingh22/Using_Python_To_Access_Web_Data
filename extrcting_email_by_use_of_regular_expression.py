import re
fname = input("Enter the File Name:")
lines = open(fname)

for line in lines:
    line = line.rstrip()
    line = re.findall("\S+@\S+",line)
    print(line)
    
#We can make it more perfect (Fine Tunning) by the use of Parnthise {i.e ()}
    line = re.findall("^From (\S+@\S+)",line)
    print(line)        
