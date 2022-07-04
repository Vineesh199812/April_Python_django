#person (name,age)
#child(place,school)
#student (roll,dept,college)

#name,age,dept,college

class Person:
    def setper(this,name,age,):
        this.name=name
        this.age=age
    def printper(this):
        print(this.name,this.age)
class Child(Person):
    def setch(this,place,school):
        this.place=place
        this.school=school
    def printch(self):
        print(self.place,self.school)
class Student(Child):
    def setstu(self,roll,dept,clg):
        self.roll=roll
        self.dept=dept
        self.clg=clg
    def printstu(self):
        print(self.name,self.age,self.dept,self.clg)

stu=Student()
stu.setper("ajay",25)
stu.setstu(1001,"bigdata","ktech")
stu.printstu()
