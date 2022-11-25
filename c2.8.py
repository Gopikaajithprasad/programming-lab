def longest(words):
	highest=0
	longest=""
	for wrd in words:
		count=0
		for a in wrd:
			count=count+1
		if(highest<count):
			highest=count
			longest=wrd
	print("longest word:",longest)
	print("number of characters:",highest)
words=input("Enter words:").split()
longest(words)
