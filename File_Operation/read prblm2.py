
f=open("numbers","r")

lst=[]
evenlst=[]
oddlst=[]

for i in f:
    lst.append(int(i.rstrip("\n")))

print(lst)

for i in lst:
    if(i%2==0):
        evenlst.append(i)
    else:
        oddlst.append(i)
print(evenlst)
print(oddlst)
print(sum(evenlst))
print(sum(oddlst))


print(sum(lst))