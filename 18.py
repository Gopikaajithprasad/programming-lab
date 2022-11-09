list1=(input("Enter colour list1:"))
clr_list1=set(list1.split(" "))
list2=(input("Enter colour list2:"))
clr_list2=set(list2.split(" "))
print(clr_list1.difference(clr_list2))

