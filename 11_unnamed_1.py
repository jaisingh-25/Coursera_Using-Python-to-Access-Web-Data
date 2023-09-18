import re

sum=0
a=open(r"...\11_unnamed_1.txt")
for i in a:
    for j in re.findall("[0-9]+", i):
        sum+= int(j)
print(sum)

# #List Comprehension short code
# import re
# #a=open(r"...\11_3_unnamed.txt")
# print(sum([int(i) for i in re.findall("[0-9]+", open(r"...\11_3_unnamed.txt").read())]))
