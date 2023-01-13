class Rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		return (self.length*self.breadth)
	def perimeter(self):
		return(2*(self.length+self.breadth))
l1=int(input("Enter l1:"))
b1=int(input("Enter b1:"))
l2=int(input("Enter l2:"))
b2=int(input("Enter b2:"))
rectangle1=Rectangle(l1,b1)
rectangle2=Rectangle(l2,b2)
if(rectangle1.area()>rectangle2.area()):
	print("rectangle1 is greater")
else:
	print("rectangle2 is greater")
	
