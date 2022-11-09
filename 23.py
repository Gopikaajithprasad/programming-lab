dic1={}
n=int(input("Enter no of keys:"))
for i in range(n):
	key=input("Enter key:")
	value=input("Enter value:")
	dic1[key]=value
print(dic1)
dic2={}
n=int(input("Enetr no of keys:"))
for i in range(n):
	key=input("Enetr key:")
	value=input("Enter value:")
	dic2[key]=value
print(dic2)
dic3={**dic1,**dic2}
for k,v in dic3.items():
	if k in dic1 and k in dic2:
		dic3[k]=[v,dic1[k]]
print(dic3)
