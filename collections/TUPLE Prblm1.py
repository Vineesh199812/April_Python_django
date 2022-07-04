#INTERVIEW QUESTION

tu=(30,45,50,55,60,65,70,75,80)
print(tu)

#update 100 in the position of 50

#tu 50====>100

#tuple is immutable
#  **Convert tuple into list and update the value then again convert the list into tuple

lst=list(tu)
lst[2]=100
print(lst)

tu=tuple(lst)
print(tu)