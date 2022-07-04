#[print range]

#[print range condition]

#syntax  ===> for morethan one condition

#[print if condition else print range] ===>elif will not workout here


#[print1 if condition1 else print2 if condition2else print3 range]

#print1 if condition1 else print2 if condition2 else print3 if condition3 else print4 range] ==>morethan 3 conditions

#prblm1
#1,50
#even square
#odd cube

#lst=[i**2 if i%2==0 else i**3 for i in range(1,51)]
#print(lst)

#prblm2
#even square
#odd print

#lst=[(i,i**2) if i%2==0 else (i,i) for i in range(1,51)]
#print(lst)
#(1,1)
#(2,4)
#(3,3)
#(4,16)............etc


#prblm3
#1,odd
#2,even

#lst=[(i,'even') if i%2==0 else (i,'odd') for i in range(1,31)]
#print(lst)

#prblm4
#even square
#divisible by 5 print 0
#odd   number

#lst=[(i**2) if i%2==0 else 0 if i%5==0 else i for i in range(1,31)]
#print(lst)

#prblm5
name='luminartechnolab'
vowes='aeiou'
#vowels print
#using list comprehension

 #lst=[i for i in name if i in vowes]
 #print(lst)

#l===>n
#u===>y
#m===>n
#i===>y

lst=[('y') if i in vowes else ('n') for i in name]
print(lst)

