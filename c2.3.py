def sumlist(l,size):
	if size==0:
		return 0
	else:
		return(l[size-1]+sumlist(l,size-1))


a=input("Enter list elements:")
a=a.split(" ")

list1=list(map(int,a))
print(list1)
print("sum is:")
total=sumlist(list1,len(list1))
print(total)
