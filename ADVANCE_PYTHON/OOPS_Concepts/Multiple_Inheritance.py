#Multiple_Inheritance       (refer cls 07/06/2022)

#child class inherit more than one parent class

class A:
    def printa(self):
        print("inside class A")
class B:
    def printb(self):
        print("inside class B")
class C(A,B):
    def printc(self):
        print("inside class C")

ob=C()
ob.printc()
ob.printb()
ob.printa()
