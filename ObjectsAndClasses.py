
class RetailItem:
	def __init__(self,unitsOnHand, price, description):
		self.unitsOnHand = unitsOnHand
		self.price = price
		self.description = description


	def decrement(self,amount):
		self.unitsOnHand -= 1

	def getPrice(self):
		return self.price
	def getUnitsOnHand(self):
		return self.unitsOnHand


watermelon = RetailItem(10, 2, "Fresh fruit")
donut = RetailItem(100, 1, "Baked good")
soda = RetailItem(36, 3, "Carbonated beverage")
total = 0
print("Would you like to buy items or look up a student?")
print("If ")
skip = input()
if(skip == "no"):
print("Would you like watermelon, soda or donut")
answer = input()
if(answer == "watermelon"):
	print("How many watermelon would you like there are ", watermelon.getUnitsOnHand())
	amount = int(input())
	watermelon.decrement(amount)
	total = watermelon.getPrice()
elif(answer == "donut"):
	print("How many donuts would you like there are ", donut.getUnitsOnHand())
	amount = int(input())
	donut.decrement(amount)
	total = donuts.getPrice()
elif(answer == "soda"):
	print("How many sodas would you like there are ", soda.getUnitsOnHand())
	amount = int(input())
	soda.decrement(amount)
	total = amount * soda.getPrice()

else:
	print("Incorrect input")
tax = total * .08
total = total + tax
print("The total cost of your purchase is: ", total)


# Struct problem 2
class Struct:
	def __init__(self, name, netID, GPA):
		self.name = name
		self.netID = netID
		self.GPA = GPA
	def getNetID(self):
		return self.netID
	def printName(self):
		print(self.name)
	def printGPA(self):
		print(self.GPA)

student1 = Struct("Matt", "ay1337", 3.5)
student2 = Struct("Jenny", "j3122", 2.0)
student3 = Struct("Clarisse", "wo2044", 4.0)
myList = [student1, student2, student3]

def getStudent(list, netid):
	for x in myList:
		if(x.getNetID() == netid):
			print("Student name:")
			x.printName()
			print("Student GPA:")
			x.printGPA()
print("Looking for student with netid of wo2044")
getStudent(myList, "wo2044")