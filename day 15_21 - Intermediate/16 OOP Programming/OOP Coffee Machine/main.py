from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

stop = False

#Print Reports
money_machine.report()
coffee_maker.report()

while not stop:
    #Check resources are sufficient
    choice = input(f'Choose your drink {menu.get_items()}\n')
    if choice == 'off':
        stop = True
    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            # process Coins
            money_machine.make_payment(drink.cost)
            # Make the coffee
            coffee_maker.make_coffee(drink)
