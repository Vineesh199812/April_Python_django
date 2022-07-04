#SET

#1. How to define

#empty {} will read as dictioanry(dict)

#how to define an empty list ==> using 'set'
st=set()

st1={1,2,3,4}

print(type(st))

st2={10,10.5,'bigdata','python'} #it supports hetrogenous data and insertion order is not preserved
print(st2)

st3={10,10,20,20,'bigdata','bigdata'} #duplicates not supported
print(st3)
# true=1 and false=0      so if we put 1 or 0 in the set it only read 1 and 0 insted of True and False because set not supports duplicate values
st4={1,2,0,3,True,False}
print(st4)
#set is mutable