
lst=[1,5,6,8,10,5,3,12,15,20]

#read value from console

#element found if value present in list

#element not found if value not in list
num=int(input("enter a number"))

for i in lst:
    if num==i:
        print("found")
        break
else:
    print("not found")
    
#it's called as linera search    
    