

#person[name,age,place]

#employee [id,dept,salary]

#student[rollno,clg]


class Person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
class Employee:
    def __init__(self,id,dept,salary):
        self.id=id
        self.dept=dept
        self.salary=salary
class Student(Person,Employee):
    def __init__(self,rollno,clg,name,age,place,id,dept,salary):
        Person.__init__(self,name,age,place)
        Employee.__init__(self,id,dept,salary)  #in multiple inheritance we use classname insted of "super" keyword
        self.rollno=rollno
        self.clg=clg
    def printstu(self):
        print(self.name,self.age,self.place,self.id,self.dept,self.salary,self.rollno,self.clg)

ob=Student("vishnu",24,"idukki",1234,"django",20000,1001,"ktech")
ob.printstu()