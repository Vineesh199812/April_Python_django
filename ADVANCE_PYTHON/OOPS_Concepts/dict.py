dic1={'ten':10,'twent':20}
dic2={'thirty':30,'fourty':40}

#merge
print(dic1)
print(dic2)

dic3={**dic1,**dic2}
print(dic3)         #to merge using **args