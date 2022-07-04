cost=int(input("enter cost price of the bike"))

if(cost>100000):
    print("tax to be paid is",(15*cost)/100)

elif(cost>50000&cost<=100000):
    print("tax to be paid is",(10*cost)/100)

else:
    print("tax to be paid is",(5*cost)/100)


