import jarvis
odds=jarvis.oddnumbers(1001**2)
i=0
sum=1
gap=1
while (odds[i]!=1001**2):
	for j in range(0,4):
			i+= gap
			sum+= odds[i]
	gap+= 1
print(sum)