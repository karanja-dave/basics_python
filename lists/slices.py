#use slices in some of the programs already created
guests=['harriet', 'jeff', 'ken', 'dave', 'caleb', 'betty', 'fridah']
#slice 1st three names 
print("The first three guests are:")
for guest in guests[:3]:
    print(guest.title())
#slice middle guests 
print("\nGuests at the middle of the invite list are:")
for guest in guests[2:5]:
    print(guest.title())
#slice last guests 
print("\nThe last guests in the list are:")
for guest in guests[-3:]:
    print(guest)

#copying items in a list
my_pizzas = ['meat deluxe','cheese burger','veg feast','chicken pepperoni']
print("Original pizza list:")
print(my_pizzas)
print("\nModified  pizza list:")
your_pizzas= my_pizzas[:]
print(your_pizzas)
#adding new items to the individaual lists
my_pizzas.append('roast veg')
your_pizzas.append('spicy boerewors')
print("\nMy favourite pizza are:")
print(my_pizzas)
print("\nYoure favourite pizza are:")
print(your_pizzas)
for pizza in your_pizzas:
    print(pizza.title())
