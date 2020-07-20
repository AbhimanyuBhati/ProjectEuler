import jarvis
primes=jarvis.primegen(1000)
primescopy=primes[:]
max=0
for b in primes:
    for a in primes:
        x=0
        while True:
            formula=x**2+a*x+b
            if formula not in primescopy:
                if(jarvis.checkprime(formula)):
                    primescopy.append(formula)
                else:
                    if (x-1)>max:
                        max=x-1
                        product=a*b
                    break 
            x+=1
        x=0
        while True:
            formula=x**2-a*x+b 
            if formula not in primescopy:
                if(jarvis.checkprime(formula) and formula>0):
                    primescopy.append(formula)
                else:
                    if (x-1)>max:
                        max=x-1
                        product=-1*a*b
                    break           
            x+=1
print(product)   


