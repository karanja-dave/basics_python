#check for inequalit
requested_topping='mushroom'
if requested_topping!='anchovies':
    print('Hold the Anchovies!\n')

#check whether value is in a list-run in terminal
requested_toppings=['mushrooms','onions','pineapple']
'mushrooms' in requested_toppings

#testing multiple conditions
requested_toppings=['mushrooms','extra cheese']
if 'mushrooms'in requested_toppings:
    print("Adding Mushrooms\n")
if 'pepperoni'in requested_toppings:
    print("Adding Pepperoni\n")
if 'extra cheese'in requested_toppings:
    print("Adding extra cheese\n")