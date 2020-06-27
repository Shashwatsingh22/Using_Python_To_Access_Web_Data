import re

#the line is given so we will extract the host from it by many ways...
line="From: stephen.marquard@uct.ac.za We will Try to nmeutralize it."

#METHOD=>1 By the help of the Slicing from the list....
#stpt=line.find("@")
#ltpt=line.find(" ",stpt)
#host=line[stpt+1:ltpt]
#print(host)

#METHOD=>2 By the help of the double split()....
#words = line.split(" ")
#email = words[1]
#peiece = email.split("@")
#host=peiece[1]
#print(host)

#METHOD=>3 By the help Regular Expression...
#line = re.findall("@([^ ]*)",line)
#print(line)
#-----<<<<<Lets Do The Fine Tunning If we know somehow what word present in front of that sentence (i.e Like Here From: )>>>---
line=re.findall("^From: .*@([^ ]*)",line)
print(line)