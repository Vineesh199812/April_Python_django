##reversing a number
#1234.......4321
#153
#153%10=3
#153//10=15
#15%10=5
#15//10=1
#1%10=1

num=int(input("enter number"))
res=0
while(num!=0):
    dig=num%10
    res=(res*10)+dig
    num=num//10
print(res)
