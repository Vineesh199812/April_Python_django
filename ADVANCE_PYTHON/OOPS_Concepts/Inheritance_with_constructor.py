

class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)

class Student(Person):
    def __init__(self,rollno,department,college,name,age,place):
        super().__init__(name,age,place)
        self.rollno=rollno
        self.department=department
        self.college=college
    def printstu(self):
        print(self.rollno,self.department,self.college)

ob=Student("ajay",24,"ekm",101,"bigdata","abc")
ob.printstu()
ob.printvalue()



#Single_inheritance [super() [child class [parents_arguments]]]
#            super().__init__(argument)