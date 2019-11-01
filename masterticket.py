"""
Excerise which shows purchase of tickets

This covers functions, while loops, try catch, exception handling, condition statements, input/output
"""

TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100


# Create the calculate price function
def calculate_price(no_of_tickets):
    return (tickets * TICKET_PRICE) + SERVICE_CHARGE


# Run this code continuously
while tickets_remaining >= 1:

    # Output how many tickets are remaining us
    print(f"There are {tickets_remaining} tickets remaining")

    # Input ask users name and assign to variable
    name = input("What is your name? ")

    # Prompt user by name and assign to new variable
    tickets = input(f"Hi {name}, how many tickets would you like? ")
    try:
        tickets = int(tickets)
        # Raise Value Error if request is more than tickets remaining
        if tickets > tickets_remaining:
            raise ValueError(f"There are only {tickets_remaining} tickets remaining")
    except ValueError as err:
        print(f"Oh no {err}, please enter an integer. Please try again!")
    else:
        # Calculate the price and assign it to variable
        price = calculate_price(tickets)

        # Output the price to screen
        print(f"Hi {name}, your ticket price is {price} pounds")

        # Prompt user if there would want to proceed
        answer = input("Would you like to proceed? ")
        # If yes
        if answer.lower() == 'y':
            # Confirm tickets are purchased
            print(f"Hi {name}, you're tickets have been confirmed")

            tickets_remaining -= tickets

        else:
            # Thank them by their name
            if answer != 'Y':
                print(f"Thank you for visiting our site {name}")

# Notify when tickets have been sold out
print(f"Sorry {name}, the tickets are all sold out")




