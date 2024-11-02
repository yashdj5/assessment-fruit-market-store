fruit_stock = {}

def add_fruit_stock():
    fruit_name = input("Enter fruit name to add: ").capitalize()
    quantity = float(input(f"Enter quantity of {fruit_name} in kg: "))
    price_per_kg = float(input(f"Enter price per kg for {fruit_name}: "))
    
    if fruit_name in fruit_stock:
        fruit_stock[fruit_name]['quantity'] += quantity
        fruit_stock[fruit_name]['price_per_kg'] = price_per_kg
    else:
        fruit_stock[fruit_name] = {'quantity': quantity, 'price_per_kg': price_per_kg}
    
    print(f"Added {quantity} kg of {fruit_name} at {price_per_kg}/- per kg.")

def view_fruit_stock():
    if fruit_stock:
        print("\nCurrent Fruit Stock (Manager View):")
        for fruit, details in fruit_stock.items():
            print(f"{fruit}: {details['quantity']} kg available at {details['price_per_kg']}/- per kg")
    else:
        print("\nNo fruit stock available.")

def update_fruit_stock():
    fruit_name = input("Enter the fruit name to update: ").capitalize()
    if fruit_name in fruit_stock:
        new_quantity = float(input(f"Enter new quantity for {fruit_name} in kg: "))
        new_price_per_kg = float(input(f"Enter new price per kg for {fruit_name}: "))
        
        fruit_stock[fruit_name]['quantity'] = new_quantity
        fruit_stock[fruit_name]['price_per_kg'] = new_price_per_kg
        
        print(f"Updated {fruit_name}: {new_quantity} kg at {new_price_per_kg}/- per kg.")
    else:
        print(f"{fruit_name} is not in stock.")

def view_and_purchase_fruits():
    if fruit_stock:
        print("\nAvailable Fruits for Purchase:")
        for fruit, details in fruit_stock.items():
            print(f"{fruit}: {details['quantity']} kg available at {details['price_per_kg']}/- per kg")
        
        while True:
            fruit_name = input("\nEnter the fruit name you want to purchase: ").capitalize()
            if fruit_name in fruit_stock and fruit_stock[fruit_name]['quantity'] > 0:
                purchase_qty = float(input(f"Enter quantity of {fruit_name} to purchase in kg: "))
                
                if purchase_qty <= fruit_stock[fruit_name]['quantity']:
                    total_price = purchase_qty * fruit_stock[fruit_name]['price_per_kg']
                    fruit_stock[fruit_name]['quantity'] -= purchase_qty
                    print(f"Purchased {purchase_qty} kg of {fruit_name} for {total_price}/-.")
                    print(f"{fruit_name} stock left: {fruit_stock[fruit_name]['quantity']} kg.")
                else:
                    print(f"Insufficient stock. Only {fruit_stock[fruit_name]['quantity']} kg available.")
            else:
                print(f"{fruit_name} is not available or out of stock.")
            
            more_purchase = input("\nDo you want to purchase another fruit? Press 'y' for yes and 'n' for no: ").lower()
            if more_purchase != 'y':
                break
    else:
        print("\nNo fruits available for purchase.")


def main_menu():
    while True:
        print("\nWelcome to the Fruit Market!")
        print("Select your role:")
        print("1) Manager")
        print("2) Customer")
        role_choice = input("Enter your choice (1/2): ")
        
        if role_choice == '1':
            while True:
                print("\nFruit Market Manager Menu:")
                print("1) Add fruit stock")
                print("2) View fruit stock")
                print("3) Update fruit stock")
                choice = input("Enter your choice (1/2/3): ")
                
                if choice == '1':
                    add_fruit_stock()
                elif choice == '2':
                    view_fruit_stock()
                elif choice == '3':
                    update_fruit_stock()
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
                
                more_operations = input("\nDo you want to perform more operations? Press 'y' for yes and 'n' for no: ").lower()
                if more_operations != 'y':
                    break
        
        elif role_choice == '2':
            
            view_and_purchase_fruits()
            more_view = input("\nDo you want to go back to the main menu? Press 'y' for yes and 'n' for no: ").lower()
            if more_view != 'y':
                break
        
        else:
            print("Invalid choice. Please enter 1 or 2.")


main_menu()
