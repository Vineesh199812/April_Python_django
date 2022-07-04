
class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place

    def printvalue(self):
        print(self.name,self.age,self.place)

class Employee(Person):
    def setemp(self,id,department,salary):
            self.id=id
            self.department=department
            self.salary=salary

    def printemp(self):
            print(self.name,self.age,self.place,self.id,self.department,self.salary)

emp=Employee()
emp.setvalue("ajay",24,'idukki')
emp.setemp(1001,"electronics",20000)
emp.printemp()