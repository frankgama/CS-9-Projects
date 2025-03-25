from menu import MenuItem, Menu



class OrderItem:
    def __init__(self, menuitem, quantity: int=1):
        self.menuitem = menuitem
        self.quantity = quantity

class Order:
    def __init__(self):
        self.order = []

    def add(self, menuitem, quantity: int = 1):
        for items in self.order:
            if items.menuitem.name == menuitem.name: 
                items.quantity += quantity
                return
        newOrderItem = OrderItem(menuitem, quantity)
        self.order.append(newOrderItem)

    def total_price(self):
        totalPrice = 0.0
        for items in self.order:
            totalPrice += items.menuitem.price * items.quantity
        return totalPrice

    def total_quantity(self):
        total_quant = 0
        for items in self.order:
            total_quant += items.quantity 
        return total_quant

    def print(self):
        
        printYourOrder = 'YOUR ORDER:'
        quant = 'Qty'
        price ='Price'
        total = 'Total'
        print_sum_total = 0
        
        print(f'{printYourOrder:<24}'+'    '+f'{quant:>3}'+ '  ' + f'{price:>8}' + '  ' + f'{total:>8}')
        
        for order_items in self.order:
            itemName = order_items.menuitem.name
            itemQuant = (order_items.quantity)
            itemPrice = order_items.menuitem.price
            totalprice = itemQuant * itemPrice
            formatPrice = f'${itemPrice:.2f}'
            formatTotal = f'${totalprice:.2f}'
        
            print(f'  {itemName:<24}' + '  ' + f'{itemQuant:>3}' + '  ' + f'{formatPrice:>8}' + '  ' + f'{formatTotal:>8}') 
            
            print_sum_total += totalprice
        
        printTOTAL = 'TOTAL'
        
        format_print_sum = f'${print_sum_total:.2f}'
        
        print(f'{printTOTAL:<39}'+'    '+ f'{format_print_sum:>8}')



# theItemsOnMenu = MenuItem("Taco", 3.50)
# newMenu = Menu()
# newMenu.add(theItemsOnMenu.name, theItemsOnMenu.price)
# newOrder = Order()
# newOrder.add(theItemsOnMenu, 1)
# newOrder.add(theItemsOnMenu, 50)
# newOrder.print()
#print(newOrder.total_quantity())
#print(newOrder.total_price())


