#identify

a=[1,2,3,4]
i=int(input("ener a index"))
try:
    print(a[i])
except Exception as e:
    print("exception occured",e)