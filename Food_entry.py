#the dict food contains many keys that represent a product, whose value is a list consisting of the expiry date, the type of food and the total amount available

from read_write import *

food = {}
def enter_food() -> None:
    """Create the dict food which holds keys representing a product, whose value is a list consisting of the expiry date, the type of food, the total amount available, and the unit
    
    >>> enter_food()
    Enter your product: milk
    Enter the type of product
    'dairy', 'vegetables and fruits', 'meat and fish', 'canned food', 'snacks','baked goods': dairy
    Unit: ml
    Enter the expiry date (mm/dd/yyyy)
    Please enter in this format with the correct date: 04/12/2020
    Enter the number of items: 2
    Enter the amount per item in product unit: 500
    Enter your product: 
    >>> food 
    {'milk': [04122020, 'dairy', 1000.0]}
    """
    condition = True
    decision = None
    while condition:
        name = input("Enter your product: ").lower()
        while name != '':
            pro_type = input("Enter the type of product\n'dairy', 'vegetables and fruits', 'meat and fish', 'canned food', 'snacks', 'baked goods': ")
            pro_type = pro_type.lower()
            if pro_type == 'dairy':
                unit = 'ml'
            elif pro_type == 'vegetables and fruits' or pro_type == 'meat and fish' or pro_type == 'canned food' or pro_type == 'snacks':
                unit = 'gram'
            elif pro_type == 'baked goods':
                unit = 'unit'
            print('Unit: ' + unit.lower())
        
            expiry_date = input("Enter the expiry date (mm/dd/yyyy)\nPlease enter in this format with the correct date: ")
            # the expiry date will be presented as a list containing the month, day, and year type int
            expiry = ''
            expiry = expiry + expiry_date[0:2] + expiry_date[3:5] + expiry_date[6:]
        
            quantity = input("Enter the number of items: ")
            amount = input("Enter the amount per item in product unit: ")
            total = float(quantity) * float(amount)
            food [name] = [expiry, pro_type, total]
            decision = input("Press X: if you are done entering\nPress Any other key: to continue\n")
            if decision == "X":
                condition = False
                break
            name = ''
    main(food)
