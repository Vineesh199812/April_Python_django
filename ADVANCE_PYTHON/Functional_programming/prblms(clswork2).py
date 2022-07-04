

#find all the numbers from 1-1000 that are divisible by 7

lst=[i for i in range(1,1001) if i%7==0]
print(lst)

#find all the numbers from 1-1000 that have a 3 in them

lst=[i for i in range(1,1001) if '3' in str(i)]
print(lst)

#count the number of spaces in a string create a list of all the consanants in the string
# "yellow yaks like yelling and yawning and yesterday they yodled while eating yuky yams"
a="yellow yaks like yelling and yawning and yesterday they yodled while eating yuky yams"
vows="aeiou"
lst=[i for i in a if i==' ']
print(len(lst))
lst1=[i for i in a if i not in 'aeiou ']
print(lst1)