f=open("C:/Users/acer/Downloads/customer","r")
#Each prof count
dic={}
for i in f:
    data=i.rstrip("\n").split(",")
    prof=data[4]
    if prof not in dic:
        dic[prof]=1
    else:
        dic[prof]+=1
print(dic)        













