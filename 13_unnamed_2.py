import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url=input("Enter Location: ")
print('Retrieving', url)
uh=urllib.request.urlopen(url, context=ctx)

data=uh.read().decode()
info= json.loads(data)
print('Retrieved', len(data), "characters")

sum=0
for item in info["comments"]:
    sum+=item["count"]
print("Count:", len(info["comments"]))
print("Sum:", sum)
