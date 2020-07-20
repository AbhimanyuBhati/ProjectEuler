import time
start=time.time()

count=1 #we start count with 1, accounting for the case that no of 200p coins is 1. Therefore, our total is met.
for g in range (0,3): #no of 100p coins
    for f in range (((200-100*g)//50)+1):#no of 50 p coins
        for e in range (((200-100*g-50*f)//20)+1): #no of 20p coins
            for d in range (((200-100*g-50*f-20*e)//10)+1): #no of 10p coins
                for c in range (((200-100*g-50*f-20*e-10*d)//5)+1): #no of 5p coins
                    for b in range (((200-100*g-50*f-20*e-10*d-5*c)//2)+1): #no of 2p coins
                        count+=1
print(count)
print(time.time()-start) 











print(time()-start)