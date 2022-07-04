

import re

s="xyzxzxzxcvxxxzxzzxzxzvcxzzxzxxx"

count=0
matcher=re.finditer('zx',s)

for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print(count)