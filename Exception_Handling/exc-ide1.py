
n1=int(input("enter number1"))
n2=int(input("enter number2"))
try:
    print(n1/n2)
except Exception as e:
    print("error",e)