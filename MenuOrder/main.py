import sys
from menu import MenuItem, Menu
from order import OrderItem, Order

def main():

    if len(sys.argv) != 2:
        print('USAGE: main.py menu.tsv')
        sys.exit(1)

    #print(type(sys.argv[1]))
    nameOfFile = sys.argv[1]
    #print(nameOfFile)

    newMenu = Menu()

    fileContents = []

    with open (nameOfFile) as file:
        next(file)
        for line in file:
            contents = line.split('\t')
            fileContents.append(contents)

    for items in fileContents:
        newMenu.add(items[0],float(items[1]))

    newMenu.print()

    newOrder = Order()

    print("\nWhat would you like to order?")


    for line in sys.stdin:

        line = line.strip()
        if line == '':
            continue

        if newMenu.find(line) == None:
            line = f'"{line}"'
            print(f"Sorry, {line} isn't on the menu.")
            continue

        menuItem = newMenu.find(line)
        #print(type(menuItem))
        newOrder.add(menuItem)

    if newOrder.total_quantity() == 0:
        exit()

    else:
        print()
        newOrder.print()



if __name__== "__main__":
    main()