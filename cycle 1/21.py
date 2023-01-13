def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print("gcd of",a,"and",b,"is:")
print(gcd(a,b))
