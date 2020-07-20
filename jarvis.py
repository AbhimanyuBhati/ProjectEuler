#Fibonnaci Generator
def fibonnaci(limit):
    fib=[]
    phi=(1+(5**0.5))/2
    for n in range (0,limit):
        entry=((phi**n)-((-1/phi)**n))/(5**0.5)
        fib.append(int(entry))
    return fib    
'''----------------------------------------------------------'''
#Prime Checker
def checkprime(x):
    if(x%2!=0 or x==2):
        for i in range(3,int(abs(x)**0.5)+1,2):
            if(x%i==0):
                return False        
        return True
    else:
        return False
'''----------------------------------------------------------'''
#Sieve of Atkin (NOT COMPLETE YET)
def atkin(limit):
    results=[2,3,5]
    sieve=[(i,False) for i in range (limit+1)] 
    for i in range (limit):
        sieve[i]=False
        x=1
        while(x*x < limit):
            y=1
            while(y*y<int(limit)):
                r=i%12
                n=(4*x*x)+(y**2)
                if((n<=limit) and (r==1 or r==5)):
                    sieve[n]=True
                n=(3*x*x)+(y**2)
                if((n<=limit)and (r==7 )):
                    sieve[n]=True
                n=(3*x*x)-(y**2)
                if((n<=limit) and (x>y) and (r==11)):
                    sieve[n]=True
                y+=1
            x+=1
        r=5
        while(r*r<limit):
            if(sieve[r]):
                for i in range(r*r,limit,r*r):
                    sieve[i]=False

    for i in range(5,limit+1):
       if(sieve[i]):
           results.append(i)
        

    #print (results)

#a = 20
#atkin(a)
'''-----------------------------------------------------------'''           

#Prime Generator using Sieve of Eratosthenes

def primegen(limit):
    results=[2,3,5,7]
    i=9
    while(i<=limit):
        if(checkprime(i)):
            results.append(i)
        i+=2           
    return results    

'''-----------------------------------------------------------'''

def primegenbeta(limit):
    results=[2]
    for i in range(3,limit,2):    
        if(checkprime(i)):
            results.append(i)           
    return results

