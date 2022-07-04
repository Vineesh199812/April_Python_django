
f=open("numbers","r")

lst=[]
for i in f:
    lst.append(int(i.rstrip("\n"))) #rstrip ===> function to remove a particular character
print(lst) #\n b'coz of next line

print(sum(lst))