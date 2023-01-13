def factor(n):
	for i in range(1,n+1):
		if(n%i==0):
			print(i)
n=int(input("Enter number"))
print("The  factor of",n,"are:")
factor(n)
