class InsufficientFundsError(Exception):
    pass

class MaximumAttemptsError(Exception):
    pass

def holiday_shopping():
    holiday_accessories = {
        'sunglasses':15,
        'jewellery': 45,
        'chanel purse': 180,
    }
    customer_budget = 100
    attempts = 0

    print("Welcome to the holiday accessories store!")
    print("These are the available items and their prices:")
    for item, price in holiday_accessories.items():
        print(f"{item}: £{price}")

    while attempts < 3:
        customer_choice = input("What item would you like to buy today? (Type 'exit' to leave the store):\n ").lower()

        if customer_choice == 'exit':
            print("Thank you for browsing. Have a nice day!")
            return

        if customer_choice not in holiday_accessories:
            raise ValueError("This item is  invalid. Please type an option again.")

        item_price = holiday_accessories[customer_choice]
        if item_price <= customer_budget:
            print(f"Here's your {customer_choice}!")
            customer_budget -= item_price
            attempts = 0  
        else:
            attempts += 1
            if attempts < 3:
                extra_money = float(input("This is not enough. Please enter the additional amount of money: "))
                customer_budget += extra_money
            else:
                raise MaximumAttemptsError("You have reached the maximum number of attempts. Exiting the shop.")

    print("Thank you for shopping with us. Goodbye!")


try:
    holiday_shopping()
except ValueError as ve:
    print(f"Error: {ve}")
except MaximumAttemptsError as mae:
    print(f"Error: {mae}")
