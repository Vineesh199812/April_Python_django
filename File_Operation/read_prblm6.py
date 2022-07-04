f=open("C:/Users/acer/Downloads/customer","r")

for i in f:
    data=i.rstrip("\n").split(",")

#age 50 above,location india,fname,lname

    if (data[3]>'50' and data[-1]=='india'):
            print(data[1:5])


