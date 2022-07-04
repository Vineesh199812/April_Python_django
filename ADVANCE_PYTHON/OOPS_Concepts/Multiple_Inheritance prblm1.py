#person [name,age]
#parent [place,phno]
#employee [id,designation,salary]

#employee : name,age,place,phno,id,designation,salary

class Person:
    def setper(this,name,age,):  #we can also use 'this' instead of 'self'
        this.name=name
        this.age=age
    def printper(this):
        print(this.name,this.age)
class Parent:
    def setpar(this,place,phno):
        this.place=place
        this.phno=phno
    def printpar(self):
        print(self.place,self.phno)
class Employee(Person,Parent):
    def setemp(self,id,des,sal):
        self.id=id
        self.des=des
        self.sal=sal
    def printemp(self):
        print(self.name,self.age,self.place,self.phno,self.id,self.des,self.sal)

emp=Employee()
emp.setper("ajay",25)
emp.setpar('idukki',333455)
emp.setemp(1001,"bigdata",25000)
emp.printemp()