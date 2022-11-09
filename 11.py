firstname=input("Enter firstNames:")
firstname=firstname.split(" ")
count=0
for i in firstname:
	for c in i:
		if c=='a':
			count=count+1
print("count of a=",count)

