# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 23:45:43 2023

@author: jaisi
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url=input("Enter - ")
html=urllib.request.urlopen(url, context=ctx).read()
soup=BeautifulSoup(html, "html.parser")

a=0
tags=soup("span")
for tag in tags:
    tag=str(tag)
    for i in re.findall("[0-9]+", tag):
        a+=int(i)
print(a)
