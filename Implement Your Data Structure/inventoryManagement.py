# Step 1: Create the inventory as an empty dictionary
inventory = {}

# Function to display the inventory
def display_inventory():
    print("\nCurrent Inventory:")
    if not inventory:
        print("Inventory is empty.")
    else:
        for item, (quantity, price) in inventory.items():
            print(f"Item: {item}, Quantity: {quantity}, Price: ${price:.2f}")

# Function to calculate the total value of the inventory
def calculate_total_value():
    total_value = 0
    for quantity, price in inventory.values():
        total_value += quantity * price
    return total_value

# Step 2: Add, Remove, and Update Items
def add_item(item_name, quantity, price):
    # Add item to the inventory
    inventory[item_name] = (quantity, price)
    print(f"Added {item_name} with quantity {quantity} and price ${price:.2f}.")

def remove_item(item_name):
    # Remove item from the inventory if it exists
    if item_name in inventory:
        del inventory[item_name]
        print(f"Removed {item_name} from the inventory.")
    else:
        print(f"{item_name} not found in inventory.")

def update_item(item_name, quantity=None, price=None):
    # Update the quantity or price of an item
    if item_name in inventory:
        current_quantity, current_price = inventory[item_name]
        new_quantity = quantity if quantity is not None else current_quantity
        new_price = price if price is not None else current_price
        inventory[item_name] = (new_quantity, new_price)
        print(f"Updated {item_name}: Quantity = {new_quantity}, Price = ${new_price:.2f}.")
    else:
        print(f"{item_name} not found in inventory.")

def main():
    inventory["apple"] = (10, 2.5)
    inventory["banana"] = (20, 1.2)
    print("Welcome to the Inventory Manager!")

    while True:
        display_inventory()
        print("\nChoose an action:")
        print("1. Add a new item")
        print("2. Remove an item")
        print("3. Update an item")
        print("4. Calculate total inventory value")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            item_name = input("Enter the name of the item: ")
            quantity = int(input(f"Enter the quantity of {item_name}: "))
            price = float(input(f"Enter the price of {item_name}: "))
            add_item(item_name, quantity, price)

        elif choice == "2":
            item_name = input("Enter the name of the item to remove: ")
            remove_item(item_name)

        elif choice == "3":
            item_name = input("Enter the name of the item to update: ")
            quantity = input(f"Enter the new quantity for {item_name} (leave blank to keep current): ")
            price = input(f"Enter the new price for {item_name} (leave blank to keep current): ")
            quantity = int(quantity) if quantity else None
            price = float(price) if price else None

            update_item(item_name, quantity, price)

        elif choice == "4":
            total_value = calculate_total_value()
            print(f"Total value of inventory: ${total_value:.2f}")

        elif choice == "5":
            print("Exiting the Inventory Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()
