#Constructor

 #constructor ==> to define instance variable in an object

#__init__
#name,age,place
class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)
pe1=Person("arun",26,'ernakulam')
pe1.printvalue()

pe2=Person("vinay",27,'kannur')
pe2.printvalue()