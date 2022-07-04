
#lst=[7,4,3,1,2]

#1. sort the given list [in ascending order]

#[1,2,3,4,7]
#low........upp

#2. Declare 2 variables

#low=0
#upp=len(lst)-1       upp=4

#3. calculate mid

#mid=(low+upp)//2    (0+4)//2=2

#Check 3 conditions

#1. search_element>lst[mid]  #4>lst[2]  4>3

        #low=mid+1

#2. Search_element<lst[mid]  #2<lst[2]  2<3

        #upp=mid-1

#3. Search==lst[mid]   #3==3  #element found


lst=[1,2,4,5,7,8,9]

lst.sort()
print(lst)

element=int(input("enter element to search"))
low=0
upp=len(lst)-1
flg=0
while (low<=upp):
    mid=(low+upp)//2
    if (element>lst[mid]):
        low=mid+1
    elif (element<lst[mid]):
        upp=mid-1
    elif (element==lst[mid]):
        flg=1
        break
if flg>0:
    print("element found")
else:
    print("element not found")
