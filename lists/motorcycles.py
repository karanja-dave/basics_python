motorcycles = ['honda','yamaha','suzuki']
#modify/change items
motorcycles[1] = 'ferari'
print(motorcycles)
#adding items
#append items to end of list
motorcycles.append('ducati')
print(motorcycles)
#add items using insert method
motorcycles.insert(0,'lamborghini')
print(motorcycles)
#remove items
#using del statment
del motorcycles[0]
print(motorcycles)
#pop () -remove last item but still use it in program
#pop can also be used to remove an item whose index is known by enclosing the items index in the pop's paranthesese 
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
#compose statment using removed item
last_bought = popped_motorcycle
print(f"The last motorcycle i bought was a {popped_motorcycle.title()}")
# remove() -removes items whose values is known
motorcycles.remove('ferari')
print(motorcycles)
#compose statments of removed items using remove()
too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"I declined a {too_expensive.title()} as I couldn't afford it")