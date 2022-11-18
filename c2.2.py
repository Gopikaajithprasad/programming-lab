def fibo(n):
	if n<=1:
		return n
	else:
		return(fibo(n-1)+fibo(n-2))

N=int(input("Enter N:"))
if N<=0:
	print("Enter a valid number")
else:
	print("Fibonacci series is:")
	for i in range(N):
		print(fibo(i))
