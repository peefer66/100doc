import os

def quantity_ingredients(dict, coffee_selection, amount_ingredients):

    pass

def main():
    ''' The main function nfor the coffee making machine.
        The user selects the coffee or Report or Off
        Check to see if there is enough ingredients, if not customer is advised
        Customer is asked for coins penny nickle dime quarters
        ingredients are de-stocked
        coffee given
        change given
     '''

    # Menu of the types of coffee available
    menu = {
        'esspresso':{'ingredients': {'water':0,'coffee':100 }, 'cost':2.0},
        'latte':{'ingredients':{'water':100, 'milk':100,'coffee':100}, 'cost':2.5},
        'cappuccino':{'ingredients':{'water':100, 'milk':100,'coffee':100}, 'cost':3.0}
    }

    ingredient_stock = {'water':100,
                        'milk':100,
                        'coffee':100}
    penny = 1 # USA coins
    nickle = 5
    dime = 10
    quarter = 25
    stop = False # Boolean to break the loop
        
    # Main loop for the coffee machine
    while not stop:
        selection = input('What coffee would you like (Espresso / Latte / Cappuccino): ').lower()
        
        # Selection
        if selection == 'off':
            stop = True
            print('Powering Off...')
        elif selection == 'report':
            print(f"Water: {ingredient_stock['water']}mls")
            print(f"Milk: {ingredient_stock['milk']}mls")
            print(f"Coffee: {ingredient_stock['coffee']}grams")
        elif selection == 'espresso':
            ingredient_stock = quantity_ingredients(menu, selection, ingredient_stock)
        elif selection == 'latte':
            pass
        elif selection == 'cappuccino':
            pass

        
main()



