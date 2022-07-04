lst=[4,3,2,1]

#6

#(2,4)
#(3,3)

#print the pair

element=int(input("enter a number"))

lst.sort()

low=0
upp=len(lst)-1

while(low<=upp):
    data=lst[low]+lst[upp]

    if(data==element):
        print("pairs are",lst[low],lst[upp])
        break
    elif(data>element):
        low=upp-1
    else:
        low=low+1