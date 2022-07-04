#kwargs : keyword arguments

#  **args

def printvalue(**args):
    return args

#print(printvalue("anu",25,"kochi"))
print(printvalue(empid=101,fname="vinay",lname="k",age=26,prof="bigdata",salary=10000))

#101 : empno
#vinay : fname
#k : lname
#26 : age
#bigdata : prof
#10000 : salary

# in **args we can print key and it's value
