#2 class

#person : name,age,place

#student : name,age,place,rollno,department

#op==> name,age,place,rollno,department

class Person:
    def setvalue(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name,self.age,self.place)

class Student(Person):
    def setstu(self,rollno,department):
        self.rollno=rollno
        self.department=department
    def printstu(self):
        print(self.name,self.age,self.place,self.rollno,self.department)

st=Student()
st.setvalue("vinay",25,'ernakulam')
st.setstu(101,"bigdata")
st.printstu()


#wok==>create 2 class and inherit it