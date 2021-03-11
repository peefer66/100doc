import os

def quantity_ingredients(menu_dict, coffee_selection, amount_ingredients):
    '''Check to determine if there is enough mterial
       for the selected coffee. if there is an updated ingredient 
       stock is returned. if not then a message telling the user 
       that it cannot make selected coffee
    '''
    for key,value in menu_dict[coffee_selection]['ingredients'].items():
        if value > amount_ingredients[key]:
            return key  
            # de-stock the ingredients          
        else:
            amount_ingredients[key] = amount_ingredients[key] -  value

    return amount_ingredients
          
def clear_screen():
    os.system('cls')

def pay_for_coffee(price):
    print(f'Price: £{price}')
    print('Please insert coins.')
    payment = 0
    payment += int(input('How many Quarters? '))*25
    payment += int(input('How many Dimes? '))*10
    payment += int(input('How many Nickles? '))*5
    payment += int(input('How many Pennies? '))*1

    return float(payment/100) # Convert payment to £


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
        'espresso':{'ingredients': {'water':50,'coffee':18 }, 'cost':1.5},
        'latte':{'ingredients':{'water':200, 'milk':150,'coffee':24}, 'cost':2.5},
        'cappuccino':{'ingredients':{'water':250, 'milk':100,'coffee':24}, 'cost':3.0}
    }

    ingredient_stock = {'water':300,
                        'milk':200,
                        'coffee':100}
   
    bank = 2.5 # Quantity of money in the machine at the start
    stop = False # Boolean to break the loop
        
    # Main loop for the coffee machine
    while not stop:
        # Clear the terminal
        #clear_screen()
        selection = str(input('What coffee would you like (Espresso / Latte / Cappuccino): ')).lower()
        # Selection
        if selection == 'off':
            stop = True
            print('Powering Off...')
        elif selection == 'report'or selection == 'r':
            print(f"Water: {ingredient_stock['water']}mls")
            print(f"Milk: {ingredient_stock['milk']}mls")
            print(f"Coffee: {ingredient_stock['coffee']}grams")
            print(f'Money in machine: {bank}')
        else:
            result = quantity_ingredients(menu,selection,ingredient_stock)
            # If the returned object is not the updated stock dictionary
            # then the returned object is the string of the low ingredient
            if type(result) == str:
                print(f'Sorry there is not enough {result} for a {selection}')
                main()
            
            # Ask for the money
            price = menu[selection]['cost']
            payment = pay_for_coffee(price)
           
            change = payment - price # Change required
            if change >=0:
                bank = bank + payment
                clear_screen()
                print(f'Here is £{change} in change. Enjoy your coffee')
                
            else:
                print(f'The price of this coffee is £{price} you only inserted £{payment}.')
  
main()      




