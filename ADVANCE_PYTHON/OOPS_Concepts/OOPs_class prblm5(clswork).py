#class:luminar

#name,roll,age,institution_name,fees

class luminar:
    institution="luminar"
    fees=29500
    def setvalue(self,name,age,rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def printvalue(self):
        print(self.name, self.age, self.rollno, luminar.institution,luminar.fees)

st1=luminar()
st1.setvalue("arun",26,101)
st1.printvalue()

st2=luminar()
st2.setvalue("vishnu",26,102)
st2.printvalue()

st3=luminar()
st3.setvalue("vinod",27,103)
st3.printvalue()