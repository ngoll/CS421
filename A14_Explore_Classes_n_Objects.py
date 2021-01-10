# Defining the class for Shoes
class Shoes:
    
    def __init__(self, name, color, size, price):
        self.name = name
        self.color = color
        self.size = size
        self.price = price

    def getDetails(self):
        print("Name : " + self.name)
        print("Color : " + self.color)
        print("Size : " + self.size)
        print("Price : " + self.price)
        

# Creating 4 instances
sneaker = Shoes("Sneaker", "Black", "8", "$25")
boot = Shoes("Boot", "Brown", "9", "$32")
converse = Shoes("Converse", "White", "6", "$30")
tennis_shoe = Shoes("Tennis Shoe", "Blue", "7", "$25")

#Getting details on 2 instances
sneaker.getDetails()
boot.getDetails()

