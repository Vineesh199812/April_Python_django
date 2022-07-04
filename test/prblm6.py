low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))

odd=0
evn=0
for i in range(low,upp+1):
    if i %2==0:
        evn+=1
    else:
        odd+=1

print("number of even numbers",evn)
print("number of odd numbers",odd)


