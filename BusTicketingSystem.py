# def bus_ticket_system():
#     destinations = {
#         'A': 10.0,
#         'B': 15.0,
#         'C': 20.0,
#         'D': 25.0,
#     }
#     locations = {
#         'A':"Tinkune",
#         'B':"Shantinagar",
#         'C':"Koteshwor",
#         'D':"Baneshwor",
#     }
#     print("Welcome to the bus ticket System!")
#     print("Please choose your destination:")

#     for place, price in destinations.items():
#         location_name = locations[place]
#         print(f"{place}:{location_name} - Rs{price:.2f}")
    
#     while True:
#         choice = input("Enter the letter of yout chosen destination: ").upper()
#         if choice in destinations:
#             selected_destination = choice
#             selected_location = locations[choice]
#             break
#         else:
#             print("Invalid choice. Please select  a valid destination.")
        
#         student_discount = 0.45
#         has_student_id = input("Do you have a student ID card? (yes/no):").strip().lower()
#         if has_student_id == 'yes':
#             ticket_price = destinations[selected_destination] *(1-student_discount)
#             print(f"with the student discount, the price for destination{selected_location}({selected_destination}) is Rs {ticket_price:.2f}.")
#         else:
#             ticket_price = destinations[selected_destination]
#             print(f"The price for destination{selected_location}({selected_destination}) is Rs{ticket_price:.2f}.")
#         total_payment = 0.0
#         while total_payment < ticket_price:
#             try:
#                 remaining_amount = ticket_price - total_payment
#                 payment = float(input(f"Enter the amount of money you are paying (Remaining: Rs{remaining_amount:.2f}):Rs"))
#                 total_payment += payment
#                 if total_payment < ticket_price:
#                     print(f"Insufficient payment. You need Rs{ticket_price-total_payment:.2f} more.")
#             except ValueError:
#                 print("Invalid input. Please enter a valid ammount.")
        
#         change = total_payment - ticket_price
#         print(f"Payment Success. Your change is Rs {change:.2f}." if change > 0 else "Payment accepted. NO change needed.")
#         print(f"Thank You for your purchase! Enjoy your trip to {selected_location}")
# bus_ticket_system()

def bus_ticket_system():
    destinations = {
        'A': 10.0,
        'B': 15.0,
        'C': 20.0,
        'D': 25.0,
    }
    locations = {
        'A': "Tinkune",
        'B': "Shantinagar",
        'C': "Koteshwor",
        'D': "Baneshwor",
    }

    print("Welcome to the Bus Ticket System!")
    print("Please choose your destination:")

    for place, price in destinations.items():
        location_name = locations[place]
        print(f"{place}: {location_name} - Rs{price:.2f}")
    
    # Choose destination
    while True:
        choice = input("Enter the letter of your chosen destination: ").upper()
        if choice in destinations:
            selected_location = locations[choice]
            break
        else:
            print("Invalid choice. Please select a valid destination.")

    # Check for student discount
    student_discount = 0.45
    has_student_id = input("Do you have a student ID card? (yes/no): ").strip().lower()
    if has_student_id == 'yes':
        ticket_price = destinations[choice] * (1 - student_discount)
        print(f"With the student discount, the price for destination {selected_location} ({choice}) is Rs{ticket_price:.2f}.")
    else:
        ticket_price = destinations[choice]
        print(f"The price for destination {selected_location} ({choice}) is Rs{ticket_price:.2f}.")

    # Payment process
    total_payment = 0.0
    while total_payment < ticket_price:
        remaining_amount = ticket_price - total_payment
        try:
            payment = float(input(f"Enter the amount of money you are paying (Remaining: Rs{remaining_amount:.2f}): Rs"))
            if payment <= 0:
                print("Payment must be greater than zero. Please try again.")
                continue
            total_payment += payment
            if total_payment < ticket_price:
                print(f"Insufficient payment. You need Rs{ticket_price - total_payment:.2f} more.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    # Calculate and display change
    change = total_payment - ticket_price
    if change > 0:
        print(f"Payment Success. Your change is Rs{change:.2f}.")
    else:
        print("Payment accepted. No change needed.")

    print(f"Thank you for your purchase! Enjoy your trip to {selected_location}.")

bus_ticket_system()
