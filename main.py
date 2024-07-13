from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino/):")

    if choice == "off":
        print("Machine turning off...")
        is_on = False

    elif choice == "report":
        resources = coffee_maker.report() # same output if not assigned in variable
        money_machine.report()

    else:
        drink = menu.find_drink(choice)
        is_resource_sufficient = coffee_maker.is_resource_sufficient(drink)

        if is_resource_sufficient:
            menu_name = menu.find_drink(choice) # same value as drink
            drink_cost = menu_name.cost
            is_transaction_successful = money_machine.make_payment(drink_cost)

            if is_transaction_successful:
                coffee_maker.make_coffee(drink)
