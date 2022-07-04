#Basic_Rules

import re
count=0
#rule='[abc]'   #it will count howmany times 'a,b,c' comes under the string
#rule='[^abc]'   #it will count except abc strings
#rule='[^a-zA-Z]'
rule='[0-9a-zA-Z]'
matcher=re.finditer(rule,'abc @sabir123')

for i in matcher:
    count+=1
    print(i.group())
    print(i.start())
print(count)