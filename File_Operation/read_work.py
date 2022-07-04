#work


#maximum temperature in every district (using dictionary)

#Temperature

#district   temperature
#dic={}
#dist=data[0]
#tem=data[1]
#if dis not in dic:  #malappuram.47
      #dic[dis]=tem
#else:
#     old_tem=dic[dic]
    #  if

f=open("C:/Users/acer/Downloads/temper","r")

dic={}
for i in f:
     data=i.rstrip("\n").split(",")
     dis=data[0]
     tem=data[1]
     if dis not in dic:
        dic[dis]=tem
     else:
         old_tem=dic[dis]
         if tem>old_tem:
              dic[dis]=tem
print(dic)