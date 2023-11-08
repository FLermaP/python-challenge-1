import os
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order=[]

# Launch the store and present a greeting to the customer
os.system('cls')
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    os.system('cls')
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    print()
    menu_selection = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_selection.isdigit():
        menu_selection=int(menu_selection)
        # Check if the customer's input is a valid option
        if menu_selection in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_selection)]
            # Print out the menu category name they selected
            os.system('cls')
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            print()
            customer_selection=input("Choose a Menu number : ")

            # 3. Check if the customer typed a number
            if customer_selection.isdigit():
                # Convert the menu selection to an integer
                customer_selection=int(customer_selection)

                # 4. Check if the menu selection is in the menu items
                if customer_selection in menu_items:
                    # Store the item name as a variable
                    item=menu_items[customer_selection]
                   
                    # Ask the customer for the quantity of the menu item
                    quantity=input("How many would you like (Invalid answers default to 1) ? ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity=int(quantity)
                    else:
                        quantity=1
                    # Add the item name, price, and quantity to the order list
                    item['Quantity']=quantity
                    order.append(item)

                # Tell the customer that their input isn't valid
                else:
                    print("Invalid Selection ")

                # Tell the customer they didn't select a menu option
                    print("That is not a valid menu option")
        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_selection} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
            
        # 5. Check the customer's input
        match keep_ordering.isalpha():
            case True:
                keep_ordering=keep_ordering.lower()
           
                match keep_ordering:
                    # Exit the keep ordering question loop
                    case 'n':
                        place_order=False
                        print("Thank you for your order ")
                        break
                    case 'y': 
                        place_order=True
                        break
                    case _:
                        print("Please Y or N only")
                        print()
                        continue

            # Complete the order
            case False:
                print("Please Y or N only")
                print()
                continue

            # Since the customer decided to stop ordering, thank them for
            # their order

            # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order
os.system('cls')
print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
# print(order)

print("Item name                 | Price    | Quantity")
print("--------------------------|----------|----------")

# 6. Loop through the items in the customer's order
for entry in order:
    # 7. Store the dictionary items as variables
    item_name = entry['Item name']
    price = entry['Price']
    quantity = entry['Quantity']
    # 8. Calculate the number of spaces for formatted printing
    name_spaces_count=26-len(item_name)
    price_spaces_count=7-len(str(price))
    quantity_spaces_count=int((9-len(str(quantity)))/2)

    # 9. Create space strings
    name_spaces = ' ' * name_spaces_count
    price_spaces = ' ' * price_spaces_count
    quantity_spaces = ' ' * quantity_spaces_count
    # 10. Print the item name, price, and quantity
    print(f"{item_name}{name_spaces}|{price_spaces}${price}  |{quantity_spaces}{quantity}")
print("--------------------------|----------|----------")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
order_cost_list=[item['Quantity']*item['Price'] for item in order]
order_cost=0
[order_cost:=order_cost+ cost for cost in order_cost_list]
print()
print(f"Thank you for your purchase, your total is ${order_cost: ,.2f}")