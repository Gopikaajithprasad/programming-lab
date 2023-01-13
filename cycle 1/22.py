n=int(input("enter the range of dictionary"))
d={}
for i in range(n):
    key=input("enter keys")
    value=input("enter values")
    d[key]=value
print(d)
print("dictionary sorted by keys:")
print("ascending order:",dict(sorted(d.items())))
print("descending order:",dict(sorted(d.items(),reverse=True)))

print("dictionary sorted by value")
print("ascending order:",dict(sorted(d.items(),key=lambda item: item[1])))
print("descending order:",dict(sorted(d.items(),key=lambda item: item[1],reverse=True)))
