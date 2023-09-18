def call_link(url):
    html=urllib.request.urlopen(url, context=ctx).read()
    soup=BeautifulSoup(html, "html.parser")
    tags=soup("a")
    a=1
    for tag in tags:
        tag=str(tag)
        if a%b==0:
            print("Retrieving:", re.findall("href=\"(.+)\"", tag)[0])
            if i==c-1:
                print("Last name -", re.findall("\">(.+)<", tag)[0])
            break
        a+=1
    return re.findall("href=\"(.+)\"", tag)[0]

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

link=input("Enter URL : ")
c=int(input("Enter count: "))
b=int(input("Enter position: "))
print("Retrieving:", link)

for i in range(c):
    link=call_link(link)
