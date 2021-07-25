##
# solving the snakes_cafe lab
##
print('''**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears
''')

##
# Ordering items 
##
Appetizers = {
    'Wings': 0,
    'Cookies': 0,
    'Spring Rolls': 0,
}
Entrees = {
    'Salmon': 0,
    'Steak': 0,
    'Meat Tornado': 0,
    'A Literal Garden': 0,
}
Desserts = {
    'Ice Cream': 0,
    'Cake': 0,
    'Pie': 0,
}
Drinks = {
    'Coffee': 0,
    'Tea': 0,
    'Unicorn Tears': 0,
}

##
# Ordering list
##

##
# menu =[{'Wings': 0, 'Cookies': 0, 'Spring Rolls': 0}, {'Salmon': 0, 'Steak': 0, '    Meat Tornado': 0, 'A Literal Garden': 0}, {'Ice Cream': 0, 'Cake': 0, 'Pie': 0}, {'Coffee': 0, 'Tea': 0, 'Unicorn Tears': 0}]
##
menu = [Appetizers,Entrees,Desserts,Drinks]



##
# start the functionality
##
user_order_confirm = input('''
***********************************
**would you like to order? Y/N**
***********************************
''').lower()
# make validation for user_order_confirm

if user_order_confirm == 'y':
    print(f'''
***********************************
** What would you like to order? **
***********************************
''')
while user_order_confirm != 'n' and user_order_confirm != 'quit':
        item = input('>>>')
        if item == 'quit':
            break  
# menu = [Appetizers,Entrees,Desserts,Drinks]
        for menu_items in menu:
            # print(menu_items.keys())
            if item in menu_items.keys():
                menu_items[item] += 1
                print(f'** {menu_items[item]} of {item} item has been added to your meal **')
                break
            else:
                print(f'enter avalid item thats includes on the menu items')
                 
else:
    input('''
**You did not order anything!**
**To quit at any time, type "quit"**
    ''')

items_available = []
for i in menu:
   items_available.append(i.items())  
print (f'''
**Your Order Summary is \n {items_available}**
''')