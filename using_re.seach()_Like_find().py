#for using the regular expression we need to first import the module
import re

name=input("Enter the Correct Name For the File(With Correct Extension):")
lines=open(name)
for line in lines:
    line=line.rstrip()
#By the Use OF the find()
#    if line.find("From:")>=0:
#        print(line)

#by the use of the re.search()
    if re.search("From:",line)>=0:
        print(line)