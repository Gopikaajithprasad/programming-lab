def string(a,b):
	new_a=b[:1]+a[1:]
	new_b=a[:1]+b[1:]
	return(new_a+' '+new_b)

a=input("Enter a string:")
b=input("Enter b string:")
print(string(a,b))
