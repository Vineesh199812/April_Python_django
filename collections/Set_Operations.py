#set_operations

#1. Union

#2. Intersection

#3. Difference


#union
#  ===> to collect all the original elements

st1={1,2,3,4,5,6,7,8}
st2={6,7,8,9,10,11,12,13,14,15}

#st1 union st2
st3=st1.union(st2)
print(st3)

#intersection

#  ==>to collect common numbers

st4=st1.intersection(st2)
print(st4)

#difference
#   ===> A-B element should present in set A and not present in set B

st5=st1.difference(st2)
print(st5)
st6=st2.difference(st1)
print(st6)