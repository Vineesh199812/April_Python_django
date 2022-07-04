student=[('viny',45),('arjun',35),('amal',65),('vipin',56)]

#highest mark name

marks=[]

for i in student:
    marks.append(i[1])
#print(marks)
#max  ==>to find maximum value

maximum=max(marks)  #65

for j in student:
    if j[1]==maximum:
        print(j[0])