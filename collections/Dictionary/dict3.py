
dic={"name":'vishnu',"age":24,"roll":101,"dept":'bigdata',"marks":30}

#marks 30===>50    to update a value
dic["marks"]+=20
print(dic)
#key : value

dic['total']=150 #To add a key and it's value

print(dic)

del dic["roll"]
print(dic)  #To delete a key value

print("name" in dic)

print("name" not in dic)

print("total" in dic)

print('vishnu' in dic)  #false
