MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}


def report(res):
    """ Prints the current resources in the coffee machine."""
    for resource, amount in res.items():
        print(f"{resource.capitalize()}: {amount}ml" if resource != "coffee" else f"{resource.capitalize()}: {amount}g")


def get_input(prompt):
    """ A function to get input from the user. If the user enters 'off', the program will terminate."""
    user_input = input(prompt).strip().lower()
    if user_input == "off":
        print("Turning off the coffee machine. Goodbye!")
        exit()  # Terminate the program
    return user_input


def check_the_resources(drink_name, menu, res):
    """ Checks if there are sufficient resources to make the selected drink.
    Returns True if resources are sufficient, otherwise False."""
    ingredients = menu[drink_name]['ingredients']
    for item, amount in ingredients.items():
        if res[item] < amount:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    quarters = int(get_input("How many quarters?:")) * 0.25
    dimes = int(get_input("How many dimes?:")) * 0.1
    nickles = int(get_input("How many nickles?:")) * 0.05
    pennies = int(get_input("How many pennies?:")) * 0.01
    current_balance = (quarters + dimes + nickles + pennies)
    return round(current_balance, 2)


def check_transaction(inserted_money, drink_cost, machine_balance):
    """ Checks if there is enough money to buy a drink. Returns True if the transaction is
     successful and updates the machine's balance."""
    if inserted_money < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False, machine_balance  # The transaction is not successful, the money is returned
    elif inserted_money == drink_cost:
        print("Transaction successful. Thank you!")
        machine_balance += drink_cost
        return True, machine_balance  # Transaction is successful, the balance is updated
    else:
        change = round(inserted_money - drink_cost, 2)  # Calculating the change
        print(f"Transaction successful. Here is ${change} in change. Thank you!")
        machine_balance += drink_cost
        return True, machine_balance


def make_coffee(drink_name, menu, resources_in_machine):
    """
    Deducts the required resources for the drink and updates the machine's inventory.
    Prints a confirmation message to the user.
    """
    ingredients = menu[drink_name]['ingredients']
    for item, amount in ingredients.items():
        resources_in_machine[item] -= amount  # Deduct the amount used for the drink
    print(f"Here is your {drink_name}. Enjoy!")


def coffee_machine():
    machine_money = 0.0  # Starting money in the machine
    while True:
        # User selection
        choice = get_input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if choice == "report":
            report(resources)
            print(f"Money: ${machine_money}")
        elif choice in MENU:
            # Check resources
            if check_the_resources(choice, MENU, resources):
                # Process coins
                inserted_money = process_coins()
                drink_cost = MENU[choice]['cost']
                # Check transaction
                success, machine_money = check_transaction(inserted_money, drink_cost, machine_money)
                if success:
                    # Make the coffee
                    make_coffee(choice, MENU, resources)
            else:
                print("Cannot process your order. Insufficient resources.")
        else:
            print("Invalid choice. Please select a valid drink.")


coffee_machine()
