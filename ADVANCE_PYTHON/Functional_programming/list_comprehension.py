#List_comprehension

#empty_list
#1to100

#lst=[]
#for i in range(1,101):
 #     lst.append(i)
#print(lst)

#lst=[print_range]

#lst=[i for i in range(1,101)]
#print(lst)

#1,75 (1,5,9,13,17,21.....)

#lst=[i for i in range(1,76,4)]
#print(lst)

#1 to 100 even numbers

#lst=[print range condition]

#lst=[i for i in range(1,101) if i%2==0]
#print(lst)

#1 to 50 odd numbers

#lst=[i for i in range(1,51) if i%2!=0]
#print(lst)

#1 to 50 even
lst=[(i,"even") for i in range(1,51) if i%2==0]
print(lst)