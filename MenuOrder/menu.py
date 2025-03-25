+#this is a menu class with the menuItem

class MenuItem:
	def __init__(self, name, price):
		self.name	= name
		self.price	= price

class Menu:

	def __init__(self):
		self.menu	= []

	def add(self, name, price):
		if self.find(name)	!=	None:
			foundItem = self.find(name)
			foundItem.price	= price
		else:
			newItem	= MenuItem(name, price)
			self.menu.append(newItem)

	def find(self, name):
		for items in self.menu:
			if items.name == name:
				return items
		return None

	def print(self):
		print("TODAY'S MENU:")
		for menuitem in self.menu:
			formattedPrice = f"${menuitem.price:>.2f}"
			print((f"  {menuitem.name:<24}") + "  " + (f"{formattedPrice:>8}"))
# fishSticks = MenuItem("Fish Sticks", "3.99")

# newMenu = Menu()

# newMenu.add(fishSticks.name, 4.99)

# newMenu.print()

# burger = MenuItem("Burger", 3.99)
# taco = MenuItem("Taco", 1.50)

# newMenu = Menu()

# newMenu.add("Burger", 3.99)
# newMenu.add("Taco", 2.00)
# newMenu.add('Burrito', 5.00)

# newMenu.print()
