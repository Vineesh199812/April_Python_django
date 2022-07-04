#lst=[1 to 75]

#even lst
#odd lst

#sum
#even sum
#odd sum

lst=[]
lst1=[]
lst2=[]

for i in range(1,76):
    lst.append(i)
    if(i%2==0):
        lst1.append(i)
    else:
        lst2.append(i)

print(lst)
print(lst1)
print(lst2)
print(sum(lst))
print(sum(lst1))
print(sum(lst2))
