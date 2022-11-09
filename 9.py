def countoccurance(str):
    count=dict()
    line=str.split()
    for i in line:
        if i in count:
            count[i]=count[i]+1
        else:
            count[i]=1
    return count
text=input("Enter line:")
print(countoccurance(text))
