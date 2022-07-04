

#map

#filter

#lst=[1,2,3,4,5,6,7,8,9,10]  f(x) ==>[1,4,9,16,25,36,49,64,81,100]   ====>map function

#[ab,ac,ce,df,gh,ip,is]    f(x) ===>[AB,AC,CE,DF,GH,IP,IS]


#filter
#[1,2,3,4,5,6,7,8,9,10]  f(x) ===>[2,4,6,8,10] *collected even nos
#[ab,ac,ce,df,gh,ip,is]  f(x) ===>[ab,ac,ce,ip,is]  *collected vowel


#syntax (for both map and filter)

#variable_name=list(map(argument1,argument2))
#variable_name=list(filter(argument1,argument2))

#argument1 ===> function
#argument2 ===> iterable


lst=[1,2,3,4,5,6,7,8,9,10]
#map
#def square(num):
 #   res=num**2
  #  return res

#data=list(map(square,lst))
#or
#data=list(map(lambda num:num**2,lst))
#print(data)


#def even(num):
#    return num%2==0 *or
#data=list(filter(lambda num:num%2==0,lst))
#print(data)

data=list(map(lambda num:num+1,lst))  #add 1
print(data)