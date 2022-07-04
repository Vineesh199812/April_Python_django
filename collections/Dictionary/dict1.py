#Dictionary

#1. How to define

dic={}

print(type(dic))

#key-value pairs

#roll:101
#name:vinay
#age:26
#dept:bigdata
#salary:10000

#key : roll,name,age,dept,salary
#values : 101,vinay,26,bigdata,10000

dic={"roll":101,"name":'vinay',"age":26,"dept":'bigdata',"salary":10000,"mark":40.5}
print(dic)

#2. heterogenous data supported

#3. duplicated values supported however duplicate keys are not supported

dic1={"roll":101,"name":'vinay',"age":26,"mark":26}
print(dic1)
dic2={"roll":101,"name":'vinay',"age":26,"age":26}
print(dic2)

#4. insertion order is preserved

#5. Dictionary is Mutable

