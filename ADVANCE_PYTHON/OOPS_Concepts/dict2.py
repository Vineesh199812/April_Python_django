employee=['vinay','anu']
default={"designation":'bigdata',"salary":10000}

#{'vinay:{designation,"salary":10000},'anu':{'designation':bigdata,salary:10000}}

#fromkeys : it returns a dictionary with specified keys and specified values

res=dict.fromkeys(employee,default)
print(res)

print(res['vinay'])

#item ===> in dict   (to print key value pairs)