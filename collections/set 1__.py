st={10,12,15,16,20,25}

# to add a single element we have to use 'add' function

st.add(50)
print(st) #we cant add it in a particular position coz insertion order is not preserved

st.add(100)
print(st)

# to add multiple elements in a set we have to use 'update' function
st.update([1,2,3,5])
print(st)