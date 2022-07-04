#name,age,prof,salary
#name===>firstname
#prof ==>print

#company
#company:luminar
#salary +5000
#key-value pairs

dic={"name":'vishnu',"age":24,"prof":'python',"salary":10000}

del dic["name"]
#dic["firstname"]='vishnu'
dic.update([("firstname","vishnu")])
print(dic)


print(dic["prof"])

dic["company"]='luminar'

dic["salary"]+=5000

for i in dic:
    print(i,dic[i])   #work