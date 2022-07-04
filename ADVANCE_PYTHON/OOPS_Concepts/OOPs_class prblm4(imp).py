#student

#name,age.rollno,college_name

#college_name ===> #static_variable  (clg name is common for all students)
#if we put a value as a static_variable then we dont have to print it separately
#we can also use "this" istead of "self"
class student:
    college="abcd"
    def setvalue(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno

    def printvalue(self):
        print(self.name,self.age,self.rollno,student.college)
st1=student()
st1.setvalue("arun",26,101)
st1.printvalue()

st2=student()
st2.setvalue("vishnu",26,102)
st2.printvalue()

