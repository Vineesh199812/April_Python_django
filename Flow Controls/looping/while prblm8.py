#lower limit
#upper limit

#sum of even num and
#sum of odd num

#2 10
#2+4+6+8+10
#3+5+7+9


low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))

even_sum=0
odd_sum=0

while(low<=upp):
    if(low%2==0):
        even_sum+=low
        low+=1
    else:
        odd_sum+=low
        low+=1
print(even_sum)
print(odd_sum)








