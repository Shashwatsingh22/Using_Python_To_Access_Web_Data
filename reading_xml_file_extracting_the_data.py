import urllib.request,urllib.parse,urllib.error
import ssl
import xml.etree.ElementTree as ET

url=input("Enter the URL:")
html=urllib.request.urlopen(url).read()

sum=0

commentinfo=ET.fromstring(html)
no_of_comments=commentinfo.findall("comments/comment")

for num in no_of_comments:
    count_=int(num.find("count").text)
    sum=sum+count_
print(sum)    