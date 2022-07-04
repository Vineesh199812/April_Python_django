
class Person:
    def setvalue(self,name,age,place):  #we can use a same value only in a function(refer class held on 03/06/202)
        self.name=name #(we can give different name ex:  self.fname=name)
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.name)
        print(self.age)
        print(self.place)
pe1=Person()
pe1.setvalue("anu",26,"kochi")
pe1.printvalue()

pe2=Person()
pe2.setvalue("arjun",30,"malappuram")
pe2.printvalue()

pe3=Person()
pe3.setvalue("vinay",34,"kannur")
pe3.printvalue()
#name
#age
#place

#self argument