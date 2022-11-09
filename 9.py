def occurence(str,word):
	a=str.split(" ")
	count=0
	for i in range(0,len(a)):
		if a[i]==word:
			count=count+1
	return count

str=input("Enter a line:")
word=input("Enter a word:")
print(occurence(str,word))
