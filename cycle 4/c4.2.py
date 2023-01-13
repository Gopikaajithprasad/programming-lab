class Account:
	def __init__(self,name,acnum,type,balance):
		self.no=acnum
		self.name=name
		self.type=type
		self.balance=balance
	def deposit(self):
		amount=float(input("Enter amount to deposit:"))
		self.balance+=amount
	def withdraw(self):
		amount=float(input("Enter amount to withdraw:"))
		if(amount>self.balance):
			print("Balance is not sufficient")
		else:
			self.balance=self.balance-amount
	def checkbalance(self):
		print("a/c balance :",self.balance)
name=input("Enter name of a/c holder:")
acnum=input("Enter a/c num:")
type=input("Enter type of a/c:")
balance=int(input("Enter balance:"))
acc1=Account(name,acnum,type,balance)
print("OPTIONS:")
print("1.DEPOSIT\n2.WITHDRAW\n3.CHECK BALANCE\n")
while(True):
	c=int(input("Enter option:"))
	if c==1:
		acc1.deposit()
	elif c==2:
		acc1.withdraw()
	elif c==3:
		acc1.checkbalance()
	else:
		break

