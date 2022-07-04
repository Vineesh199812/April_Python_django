#student
#name,rollno,department,clpllege_name
#3 students

class Student:
    def setvalue(self,name,rollno,department,college_name):
        self.fname=name
        self.rollno=rollno
        self.department=department
        self.college_name=college_name
    def printvalue(self):
        print(self.fname,self.rollno,self.department,self.college_name)

st1=Student()
st1.setvalue("vishnu",1001,"python","luminar")
st1.printvalue()

st2=Student()
st2.setvalue("vonod",1002,"django","luminar")
st2.printvalue()

st3=Student()
st3.setvalue("vijay",1003,"bigdata","luminar")
st3.printvalue()

