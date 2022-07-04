#employee
#argument: name,id,designation,salary,company

class Employee:
    def setvalue(self,name,id,desig,sal,company):
        self.fname=name
        self.id=id
        self.desig=desig
        self.sal=sal
        self.comp=company
    def printvalue(self):
        print(self.fname,self.id,self.desig,self.sal,self.comp)

em1=Employee()
em1.setvalue("vishnu",1001,"car",10000,"tata")
em1.printvalue()

em2=Employee()
em2.setvalue("vineesh",1002,"suv",12000,"tata")
em2.printvalue()

#work! ==> remove special characters and then word count
#work ==> remove special characters and print
#most frequent word




