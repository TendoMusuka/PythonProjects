from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def check_off_requested(message):
    if message == 'off':
        print("Machine off")
    if message == ' report':
        CoffeeMaker.report()


choice_of_coffee = input("“What would you like? (espresso/latte/cappuccino/):")
able_to_make_drink = CoffeeMaker.is_resource_sufficient(choice_of_coffee)

if able_to_make_drink :
    CoffeeMaker.make_coffee(choice_of_coffee)
else:
    for ingredeients in Menu

