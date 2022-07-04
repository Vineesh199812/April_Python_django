class A:
    def printa(self):
        print("inside class A")
class B(A):
    def printa(self):
        print("inside class B")
#ob=B()
#ob.printa() #Here the method executing is method overriding
class C(B):
    def printa(self):
        print("inside class C")

ob=C()
ob.printa()     #the last child class will execute in method overridinf
