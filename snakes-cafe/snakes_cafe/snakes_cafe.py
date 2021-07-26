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
    'wings': 0,
    'cookies': 0,
    'spring rolls': 0,
}
Entrees = {
    'salmon': 0,
    'steak': 0,
    'meat tornado': 0,
    'a literal garden': 0,
}
Desserts = {
    'ice cream': 0,
    'cake': 0,
    'pie': 0,
}
Drinks = {
    'coffee': 0,
    'tea': 0,
    'unicorn tears': 0,
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


##
# start the function
##
print('''
***********************************
** What would you like to order? **
***********************************
''')
user_order = input('enter item name >>> ').lower()
while user_order != 'quit':
    flag = False
    for menu_object in menu:
        for object_key in menu_object.keys():
            if object_key == user_order:
                flag = True
                menu_object[user_order]+=1
                print(f'**{menu_object[user_order]} order of {user_order} have been added to your meal **')
    if not flag:  
        print('''
        ** Your item is not in the menu for now **\n
        ** we will add this soon to our menu **
        ''')

    user_order=input('order another item >>>')
    

print(menu)
