#Regular_Expression

#It's a Python Package

#Pattern Matching

#String

#Validation

#   ====> to create a password that contains specific characters(refer cls 14/06/2022)
#   ====> to give a phn number only in 10 digit format

import re
s="abaaaaabbbbabaabab"

#finditer

#finditer(argument1,argument2)

#argument1: find_pattern

#argument2: string_name
#ab
count=0
matcher=re.finditer('ab',s)

for i in matcher:
    count+=1
    print(i.group())   #to find which string is matching
    print(i.start())   #to find index
print(count)