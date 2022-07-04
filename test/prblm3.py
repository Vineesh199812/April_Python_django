#prime number btwn 1 to 100


for i in range(1,100+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break

        else:
            print(i)
