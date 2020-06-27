import re
fname = input("Enter the fileName: ")
lines = open(fname)
for line in lines:
    line = line.rstrip()
#    if re.search("^From:",line):
#       print(line)

#this Same thing can also be done by the help of startswith()
    if line.startswith("From:"):
        print(line)
         