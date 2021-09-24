from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def get_report():
    coffee_maker.report()


def turn_off():
    print("turning off the machine...")


def display_menu(p_menu):
    print(p_menu.get_items())


def process_coffee_order(order):
    if coffee_maker.is_resource_sufficient(order):
        cost = order.cost
        if money_machine.make_payment(cost):
            coffee_maker.make_coffee(order)

    else:
        print(f"Sorry there is not enough ingredients")


def display_menu():
    for menu_item in menu.menu:
        print(f"{menu_item.name} : ${menu_item.cost} ")


def apply_command(command):
    if command == "report":
        get_report()
        return True
    elif command == "menu":
        display_menu()
        return True
    elif command in ["espresso", "latte", "cappuccino"]:
        process_coffee_order(menu.find_drink(command))
        return True
    elif command == "off":
        turn_off()
        return False
    else:
        return True


def main():
    while True:
        command = input("What would you like? (espresso/latte/cappuccino): ").lower()

        action = apply_command(command)

        if not action:
            return


main()


