#check given number is prime number or not

num=int(input("enter a number"))
x=0
for i in range(1,num+1):
    if(num%i==0):
        x+=1
if (x==2):
    print(num,"is a prime number")
else:
    print(num,"is not a prime number")
    