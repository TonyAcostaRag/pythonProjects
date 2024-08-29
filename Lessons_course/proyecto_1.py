# This is a sample Python script.
import time

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

from functools import reduce
from datetime import datetime
import statistics

def add_Item():

    name_Item = input('\nEnter the item name: ')
    amount_Item = input(f'Enter the quantity of the item {name_Item}: ')
    price_Item = input(f'Enter the unit price of the item {name_Item}: ')
    type_item = input(f'Enter the type of the item {name_Item}: ')
    size_Item = input(f'Enter the size of the item {name_Item}: ')

    tstamp = datetime.now()

    item = {
        'name' : name_Item,
        'amount' : amount_Item,
        'unit price' : price_Item,
        'type' : type_item,
        'size' : size_Item,
        'timestamp' : "{}/{}/{} ".format(tstamp.year, tstamp.month, tstamp.day)
                      + "{}:{}:{}".format(tstamp.hour, tstamp.minute, tstamp.second)
    }

    items.append(item)
    print(f'Item added.\nInfo of the item: ', item)

    print('\nAll the items in inventory: ', items)

def update_Item():
    name_Item = input('\nEnter the item name to update: ')
    for item in items:
        if item['name'] == name_Item:
            name = input('Enter the new name: ')
            quantity = input('Enter the new quantity: ')
            unit_price = input('Enter the new unit price: ')
            type = input('Enter the new type: ')
            size = input('Enter the new size: ')

            item['name'] = name
            item['amount'] = quantity
            item['unit price'] = unit_price
            item['type'] = type
            item['size'] = size

            print(f'Item updated.\nInfo of the item: ', item)
            #return
        else:
            print('Item not found.')

    print('\nAll the items in inventory: ', items)
    return

def search_item():
    option = int(input('\nSearch by:'
                       '\n1. Item name'
                       '\n2. Item amount'
                       '\n3. Item unit price'
                       '\n4. Item type'
                       '\n5. Item size'
                       '\nEnter Option: '))

    if option == 1:
        item_Name = input('Enter item name to search: ')
        filtered_item = list(filter(lambda item: item_Name.lower() in item['name'].lower(), items))
    elif option == 2:
        amount = input('Enter item mount to search: ')
        filtered_item = list(filter(lambda item: amount.lower() in item['amount'].lower(), items))
    elif option == 3:
        unit_price = input('Enter item unit price to search: ')
        filtered_item = list(filter(lambda item: unit_price.lower() in item['unit price'].lower(), items))
    elif option == 4:
        item_type = input('Enter item type to search: ')
        filtered_item = list(filter(lambda item: item_type.lower() in item['type'].lower(), items))
    elif option == 5:
        item_size = input('Enter item size to search: ')
        filtered_item = list(filter(lambda item: item_size.lower() in item['size'].lower(), items))
    else:
        print('Invalid option.')
        return

    if len(filtered_item) > 0 :
        print('Search results:')
        print(f'Items found: {filtered_item}')
    else:
        print('No items found.')

def sort_items():
    option = int(input('Sort by:'
                       '\n1. Item name'
                       '\n2. Item amount'
                       '\n3. Item unit price'
                       '\n4. Item type'
                       '\n5. Item size'
                       '\nEnter option: '))

    if option == 1:
        sorted_item = sorted(items, key=lambda item: item['name'])
    elif option == 2:
        sorted_item = sorted(items, key=lambda item: item['amount'])
    elif option == 3:
        sorted_item = sorted(items, key=lambda item: item['unit price'])
    elif option == 4:
        sorted_item = sorted(items, key=lambda item: item['type'])
    elif option == 5:
        sorted_item = sorted(items, key=lambda item: item['size'])
    else:
        print('Imvalid option.')
        return

    print('Sorted items:')
    print(sorted_item)

def inventory_management(action):

    def calculate_inventoryValue():
        print('Inventory value: ', reduce( lambda a, b: a + b, [ (int(item['amount']) * float(item['unit price'])) for item in items ] ))

    def display_items():
        print('1. Display all the items available by name')
        print('2. Display all the types availables')

        option = int(input('Enter the display option: '))

        if option == 1:
            print(list(map(lambda item: item['name'], items)))
        elif option == 2:
            print(list(map(lambda item: item['type'], items)))
        else:
            print('Invalid option.')
            return

    if action == 1:
        return calculate_inventoryValue
    elif action == 2:
        return display_items

def deleting_item():
    item_Name = input('Enter item name to delete: ')
    filtered_item = list(filter(lambda item: item_Name.lower() in item['name'].lower(), items))

    if len(filtered_item) > 0:
        print(f'Item to delete: {filtered_item}')
        confirm = int(input('Confirm by pressing 1 to delete: '))

        if confirm == 1:
            name = filtered_item[0]['name']
            print(f'Deleting name {name}')

            items[:] = [item for item in items if item['name'] != name]
            print('Item deleted.')

            """
            for dictionary in items:
                for key, value in dictionary.items():
                    if key == 'name':
                        if value == name:
                            items.remove(items[key][value])"""

            #items.remove(name)
    else:
        print('No items were found.')


def show_Statistics(action):

    def amounts_statistics():
        print('All the amounts per item: ', [( int(item['amount']) ) for item in items])
        print('The mean of the items amounts: ', statistics.mean([( int(item['amount']) ) for item in items]))
        print('The median of the items amounts: ', statistics.median([(int(item['amount'])) for item in items]))
        print('The standard deviation of the items amounts: ', statistics.stdev([(int(item['amount'])) for item in items]))

    def money_statistics():
        print('All the unit price per item: ', [(float(item['unit price'])) for item in items])
        print('The mean of the items unit price: ', statistics.mean([(float(item['unit price'])) for item in items]))
        print('The median of the items unit price: ', statistics.median([(float(item['unit price'])) for item in items]))
        print('The standard deviation of the items unit price: ', statistics.stdev([(float(item['unit price'])) for item in items]))

    if action == 1:
        return amounts_statistics
    elif action == 2:
        return money_statistics

def displayItem_ByType():
    print(list(map(lambda item: item['type'], items)))
    selectedType = input('Enter the expected type to search from the options above: ')
    itemsType = [(item['name']) for item in items if item['type'] == selectedType ]
    print(f'List of items by type {selectedType}: {itemsType}')

def item_menu():
    while True:
        print('\n-- Item Management System ---')
        print('1. Add New Item')
        print('2. Update amounts')
        print('3. Search Items')
        print('4. Sort Items')
        print('5. Delete Item')
        print('6. Inventory management')
        print('7. Inventory statistics')
        print('8. Display items by type')
        print('10. Exit')

        choice = int(input('\nEnter your choice: '))

        if choice == 1:
            print('Adding item')
            add_Item()
        elif choice == 2:
            print('Updating item')
            update_Item()
        elif choice == 3:
            print('Searching item')
            search_item()
        elif choice == 4:
            print('Sorting item')
            sort_items()
        elif choice == 5:
            print('Deleting item')
            deleting_item()
        elif choice == 6:
            print('\nInventory management')
            print('1. Calculate the total inventory value')
            print('2. Display available items')
            action = int(input('Enter the management option: '))
            f = inventory_management(action)
            f()
        elif choice == 7:
            print('\nShow inventory statistics')
            print('1. Amounts statistics')
            print('2. Money statistics')
            action = int(input('Enter the statistics option: '))
            st = show_Statistics(action)
            st()
        elif choice == 8:
            print('\nDisplay items by type')
            displayItem_ByType()
        elif choice == 10:
            print('Exiting...')
            break
        else:
            print('Invalid option. Try again')

items = []

item_menu()
