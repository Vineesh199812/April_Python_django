#current year
#current month
#current date


#birth year
#birth month
#birth year


#age print

#age=current year - birth year

crnt_year=int(input("enter current year"))
birth_year=int(input("enter birth year"))
crnt_month=int(input("enter current month"))
birth_month=int(input("enter birth month"))
crnt_date=int(input("enter current date"))
birth_date=int(input("enter birth date"))
age=crnt_year-birth_year
if(crnt_year>birth_year):
    if(crnt_month>=birth_month):
        print("your age is",age)
    elif(crnt_date>=birth_date):
        print("your age is",age)
    else:
        print("your age is",age-1)

