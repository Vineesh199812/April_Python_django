#method overloading : same method name , different number of arguments (refer cls 08/06/2022)

class Add:
    def sum(self,num1,num2):
        self.num1=num2
        self.num2=num2
        print(self.num1+self.num2)
class Add1(Add):
    def sum(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)   #python doesn't support method overloading
                                               #instead it takes the most latest method here it is "Add1"

ob=Add1()
#ob.sum(5,6)
ob.sum(4,5,6)