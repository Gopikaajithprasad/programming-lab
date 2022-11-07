y={'sree':'25','mani':'40','rohan':'35'}
l=list(y.items())
l.sort()
print("ascending order is:",l)
l.sort(reverse=True)
print("descending order is",l)
dict=dict(l)
print("dictionary",dict)
