#Wordcount


#cat rat cat bat rat cat bus bus car car

#total count=10

#cat,3
#rat,2
#bat,1
#bus,2
#car,2

line='cat rat bus cat car car rat bus car car bus cat'

#1. line of data convert into word by word data

#split ==> using split function

print(line)
data=line.split(' ')
print(data)

dic={}
#key   value
#cat,1+1=2
#rat,1
#bus,1
#car,1+1=2

for i in data: #cat rat bus
    if i not in dic: #cat rat bus cat
        dic[i]=1 #cat,1 rat,1 bus,1
    else:
        dic[i]+=1

print(dic)












