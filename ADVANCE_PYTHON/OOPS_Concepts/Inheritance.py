#Inheritance

#parent

#child      ==>child should collect the properties of parent

#class A (parent)
#class B (child)    ==>methods and variables   *cls B can use cls A's methods and variables(refer 06/06/2022 cls)

class A:
    def printa(self,num1):  #Parent_class OR Base_class OR Super_class
        self.num1=num1
        print("inside class A",self.num1)

class B(A):
    def printb(self,num2):  #Child_class OR Sub_class OR Derived_class
        self.num2=num2
        print("inside class B",self.num2,self.num1)

#a=A()
#a.printa(10)
b=B()
b.printa(40)
b.printb(50)


