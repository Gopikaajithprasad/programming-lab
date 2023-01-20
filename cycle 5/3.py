import csv
with open("sample.csv",mode="r")as ob:
	csvfile=csv.reader(ob)
	for x in ob:
		L=x.rstrip().split(",")
		print(L)
