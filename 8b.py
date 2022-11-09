a=input("Enter the number of list:")
a=a.split(" ")
a=list(map(int,a))
print(a)
b=[x*x for x in a if x>0]
print(b)
