master_string="abbcddeghgggt"
chk_word="egg"

res=""

wc={}
for char in master_string:
    if char in wc:
        wc[char]+=1
    else:
        wc[char]=1

for char in chk_word:
    if char in wc:
        curCount=wc.get(char)
        if curCount>0:
            res+=char
            wc[char]-=1
        else:
            break
print(res==chk_word)