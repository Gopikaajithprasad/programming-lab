def common_element(a, b):
    list_1 = set(a)
    list_2 = set(b)
    if (list_1 & list_2):
        print(list_1 & list_2)
    else:
        print("There are no common elements")
 

a=input("Enter list1 elements:")
a=a.split(" ")
a=list(map(int,a))
b=input("Enter list2 elements:")
b=b.split(" ")
b=list(map(int,b))
print(a)
print(b)

#ckeck whether length of list are equal

l1=len(a)
l2=len(b)
if(l1==l2):
	print("list1 and list2 are of same length")
	l=l1=l2
	print("length of list is",+l)
else:
	print("list1 and list2 are not same length")

#check whether sums are equal

if(sum(a)==sum(b)):
	print("list1 and list sums are equal")
	s=sum(a)
	print("sum=",s)
else:
	print("sums are not equal")

#check whetherany value occurs in both
print("Common values are:")
common_element(a, b)
 







