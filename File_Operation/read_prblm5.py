f=open("C:/Users/acer/Downloads/customer","r")

for i in f:
    data=i.rstrip("\n").split(",")

#age above 50,fname,lname,age,prof
    for i in data:
         if(data[3]>'50'):
            print(data[1:5])
            break
