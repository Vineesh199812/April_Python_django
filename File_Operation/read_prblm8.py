f=open("C:/Users/acer/Downloads/customer","r")
#each location count
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    loc=data[-1]
    if loc not in dic:
        dic[loc]=1
    else:
        dic[loc]+=1
print(dic)
