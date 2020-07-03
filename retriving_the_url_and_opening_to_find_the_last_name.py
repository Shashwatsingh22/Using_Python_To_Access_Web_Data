import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter the URL:")
count=int(input("Count:"))
position=int(input("Position: "))

for i in range(count):
    html=urllib.request.urlopen(url,context=ctx).read()
    soup=BeautifulSoup(html,'html.parser')
    tags=soup('a')
    suburl=list()
    tx=list()

    for tag in tags:
        url=tag.get('href',None)
        text=tag.text
        suburl.append(url)
        tx.append(text)
    print(suburl[position-1])
    print(tx[position-1])
    url=suburl[position-1]