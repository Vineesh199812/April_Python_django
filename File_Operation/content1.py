#file read
#special
#
f=open("content","r")

sc="!@#$%^&*(){}"
for i in f:
    data=i.rstrip("\n")
    string=""
    for j in data:
        if j not in sc:
            string+=j
    print(string)


#here is a pending work ==>refer to oops concepts section