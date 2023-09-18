import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter location: ")
print("Retrieving", url)
data = urllib.request.urlopen(url, context=ctx).read()
print("Retrieved", len(data), "characters")

tree=ET.fromstring(data)
counts=tree.findall(".//count")
sum=0
for i in counts:
    sum+=int(i.text)
print("Count:", len(counts))
print("Sum:", sum)
