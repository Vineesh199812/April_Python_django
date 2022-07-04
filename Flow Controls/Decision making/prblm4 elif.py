sub1=int(input("enter marks of subject1"))
sub2=int(input("enter marks of subject2"))
sub3=int(input("enter marks of subject3"))
sub4=int(input("enter marks of subject4"))
total=sub1+sub2+sub3+sub4
print(total)

if(total>=180):
    print("grade is A+")

elif(total>=160)&(total<=179):  #or 160<=total<=179
    print("grade is A")

elif(total>=140)&(total<=159):
    print("grade is B+")

elif(total>=120)&(total<=139):
    print("grade is B")

elif(total>=100)&(total<=119):
    print("grade is C+")

elif(total>=140)&(total<=159):
    print("grade is C")

else:
    print("FAIL")


