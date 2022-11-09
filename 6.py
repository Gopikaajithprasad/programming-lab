start=2022
endyear=int(input("Enter end year:"))
for i in range(start,endyear):
	if i%4==0 and i%100!=0 or i%400==0:
		print(i)
