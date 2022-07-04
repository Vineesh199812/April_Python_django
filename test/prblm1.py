#palindrome

str=input("enter word")

if(str==str[::-1]):
    print("palindrome")
else:
    print("not palindrome")