def menu_system():
    food = {
        'MoMo': 200,
        'Chowmein': 160,
        'Sausage': 150,
        'Slice': 100,
        'Coke': 100,
        'Burger': 120,
        'Thai': 1300,
        'Korean': 1200,
        'Thakali': 1000,
    }
    # Mapping for menu item abbreviations (optional if you want to use codes)
    menu_codes = {
        'A': 'MoMo',
        'B': 'Chowmein',
        'C': 'Sausage',
        'D': 'Slice',
        'E': 'Coke',
        'F': 'Burger',
        'G': 'Thai',
        'H': 'Korean',
        'I': 'Thakali',
    }
    
    print("Welcome to the Restaurant Menu System!")
    print("Here is our menu:")
    print("-" * 30)

    for code, item in menu_codes.items():
        price = food[item]
        print(f"{code}: {item} - Rs{price:.2f}")

    print("-" * 30)
    print("Please select your food by corresponding letters. Enter'done' when you are finished.")

    selected_items = []
    while True:
        choice = input("Enter your choice (or 'done' to finish): ").strip().upper()
        if choice == 'DONE':
            break
        elif choice in menu_codes:
            selected_items.append(menu_codes[choice])
            print(f"{menu_codes[choice]} added to your order.")
        else:
            print("Invalid choice. Please select a valid item.")
    if not selected_items:
        print("No items selected. Thank you for visiting!.")
        return
    
    #calulate the total price
    subtotal = sum(food[item] for item in selected_items)
    vat = subtotal * 0.13
    service_tax = subtotal * 0.05
    total = subtotal + vat + service_tax

    # Print the bill
    print("\n Your Bill:")
    print("-"* 30)
    for item in selected_items:
        print(f"{item}: Rs{food[item]:.2f}")
    print("-" * 30)
    print(f"Subtotal: Rs{subtotal:.2f}")
    print(f"VAT (13%): Rs{vat:.2f}")
    print(f"Service Tax (5%): Rs {service_tax:.2f}")
    print(f"Total: Rs{total:.2f}")
    print("Thank you for your order Enjoy your food.")


menu_system()