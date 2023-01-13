a=[]
n=input("Enter numbers:").split()
for i in n:
	if int(i)>100:
		a.append("over")
	else:
		a.append(i)
print(a)
