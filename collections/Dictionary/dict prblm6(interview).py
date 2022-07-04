n=""
print(type(n))

ex=input("enter a string")#apple
ex1=""
vow="aeiouAEIOU"
for i in ex:
    if i not in vow:
        ex1+=i
print(ex1)
