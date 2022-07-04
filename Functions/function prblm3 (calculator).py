def sum(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

print("1.addition\n"
      "2.substraction\n"
      "3.multiplication\n"
      "4.division")

choice=int(input("enter choice"))
num1=int(input("enter number1"))
num2=int(input("enter number2"))

if choice==1:
    print(num1,'+',num2,'=',sum(num1,num2))
elif choice==2:
    print(num1,'-',num2,'=',sub(num1,num2))
elif choice==3:
    print(num1,'*',num2,'=',mul(num1,num2))
elif choice==4:
    print(num1,'/',num2,'=',div(num1,num2))
else:
    print("invalid")


