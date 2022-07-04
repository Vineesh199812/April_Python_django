
class Employee:
    def __init__(self,id,fname,lname,age,prof,place):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.age=age
        self.prof=prof
        self.place=place
    def printval(self):
        print(self.id,self.fname,self.lname,self.age,self.prof,self.place)

f=open("C:/Users/acer/Downloads/customer","r")
for i in f:
    data=i.rstrip("\n").split(",")
    id=data[0]
    fname=data[1]
    lname=data[2]
    age=data[3]
    prof=data[4]
    place=data[-1]

    ob=Employee(id,fname,lname,age,prof,place)
    #ob.printval()
    #print(ob.fname,ob.lname)


    #name,lname,age,prof