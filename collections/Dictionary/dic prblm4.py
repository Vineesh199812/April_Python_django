pattern='ABCDBCDEF'

#1. First recursive character ==>repeating character  #B

#dic={}

#A,1
#B,1
#C,1
#D,1
#B
dic={}

for i in pattern:
    if i not in dic:
        dic[i]=1
    else:
        print("first recursive character is",i)
        break

