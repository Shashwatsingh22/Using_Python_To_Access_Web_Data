import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter the URL:")
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')

summ=0
tags=soup('span')
for num in tags:
    num=int(num.text)
    summ=summ+num
print(summ) 