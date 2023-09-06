# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 16:12:01 2023

@author: jaisi
"""

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
# print(sum([int(i) for i in re.findall("[0-9]+", open(r"C:\Users\jaisi\Documents\Jai\Coursera\Python for Everybody - Specialisation\3_Using Python to Access Web Data\11_3_unnamed.txt").read())]))
