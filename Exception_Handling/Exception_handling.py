#Exception handling
#To handle unexpected errors

num1=int(input("enter number1"))
num2=int(input("enter number2"))
#print(num1/num2) #6/0

try:
    print(num1/num2)  #chance of error
except:
    print("zero division error") #soluton of error
finally:
    print("inside") #does nothing
#3 blocks

#try   : divide
#except: zero
#finally