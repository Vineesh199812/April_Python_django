
#1.create a list from element of a range from 1200 to 2000 with steps of 130

#2. lst=[44,54,64,74,104]
  #lst1=[50,60,70,80,110

#3. 1,15 [element square greaterthan 50]

#1..
lst=[(i) for i in range(1200,2001,130) ]
print(lst)

#2..
lst=[44,54,64,74,104]
lst1=[i+6 for i in lst]
print(lst1)

#3..
lst=[i for i in range(1,16) if i**2>50]
print(lst)

#4..
dic={"sedan":1500,"suv":2000,"pickup":2500,"minivan":1600,"van":2400,"semi":13600,"bicycle":7}
#weight above 2000 ===> print
#uppercase
lst=[i.upper() for i in dic if dic[i]>2000] #===> convert intp upper using 'upper()' function
print(lst)
