

lst=[1,5,6,8,10,5,3,12,15,20]
num=int(input("enter a number"))
flg=0
for i in lst:
    if num==i:
        flg=1
        break
if(flg>0):
    print("found")
else:
    print("not found")

#it's called as linear search

#drawback

#complexicty

#instead we can use Binary search