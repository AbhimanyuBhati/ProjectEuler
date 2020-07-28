sum1=0
for g in range (0,10):
    for h in range (0,10):
        for i in range (0,10):
            for j in range (0,10):
                for k in range (0,10):
                    for l in range (0,10):
                        num=(g**5)+(h**5)+(i**5)+(j**5)+(k**5)+(l**5)
                        compare=(g*100000)+(h*10000)+(i*1000)+(j*100)+(k*10)+l
                        #sumdig=g+h+i+j+k+l
                        if(num==compare and num!=1):
                            sum1=sum1+num
print(sum1)