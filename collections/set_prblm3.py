st={10,20,30,40,50,60,70,80,90,100}

print(st)

# remove ===> to remove an element in a set

st.remove(30)
print(st)

#or

#discard ===> to remove an element in set

st.discard(80)
print(st)

#difference btwn. 'remove' and 'discard'

st.remove(150) #===> remove ===>it's return type
print(st)

st.discard(150) #===> discard ===> it's not return type
print(st)