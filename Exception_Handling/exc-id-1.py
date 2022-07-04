#how to generate an exception

age=int(input("enter ur age"))

if age>=18:
    print("eligible")
else:
    raise Exception("not allowed")