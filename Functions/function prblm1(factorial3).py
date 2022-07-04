def fact(num):
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    return fac
data=fact(5)

print(data)