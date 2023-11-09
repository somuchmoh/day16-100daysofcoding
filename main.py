from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
make_coffee = CoffeeMaker()
get_money = MoneyMachine()

in_menu = menu.get_items()
machine_ready = True
while machine_ready:
    order_name = input(f"What would you like? {in_menu}: ")

    if order_name == 'report':
        make_coffee.report()
        get_money.report()
    else:
        menu_item = menu.find_drink(order_name=order_name)
        if make_coffee.is_resource_sufficient(drink=menu_item):
            cost = menu_item.__getattribute__('cost')
            if get_money.make_payment(cost=cost):
                make_coffee.make_coffee(order=menu_item)
        else:
            machine_ready = False
