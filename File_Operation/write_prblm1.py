f=open("data","r")
f1=open("data_copy","w")

for i in f:
    f1.write(i)


    #append ====> use 'a' instead of 'w'