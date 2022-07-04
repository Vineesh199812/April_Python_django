f=open("C:/Users/acer/Downloads/customer","r")

for i in f:
     data=i.rstrip("\n").split(",")
     #fname,lname,age
     #
     fname=data[1]
     lname=data[2]
     age=data[3]
     print(fname,",",lname,",",age)
     #OR
     #print(data[1:4])
     #print(data[0:4:2])