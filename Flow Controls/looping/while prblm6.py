#lower
#upper
#print even numbers btwn lower and upper

low=int(input("enetr lower number"))
upp=int(input("enter upper number"))

while(low<=upp):
    if(low%2==0):
        print(low)
    low+=1
