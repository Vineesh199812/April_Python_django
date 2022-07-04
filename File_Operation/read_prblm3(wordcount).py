
f=open("paragraph","r")
dic={}
for i in f:
    data=i.rstrip("\n").split(" ")
    for i in data:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
print(dic)

#for i in dic:
    #print(i,",",dic[i])

    #OR
for k,v in dic.items(): # items ===> to print key value pairs
    print(k,",",v)

