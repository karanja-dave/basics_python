#0rganizing lists
cars = ['bmw','audi','toyota','subaru']
#sorting lists permanently sort() -sorts lists based on alphabetical order
#descending order (A-Z)
cars.sort()
print(cars)
#ascending order
cars.sort(reverse=True) #argument reverse=True is used to give the ascending alphabetical order
print(cars)
#sorting lists temporarily
#descending order
cars = ['bmw','audi','toyota','subaru']
print("Here's the original order:" )
print(cars)
print("Here's the sorted order:")
print(sorted(cars))
#printing a list in reverse order -~based on alphabetical order but the index of the items in the list
cars.reverse()
print(cars)
#finding length of list -know number of items in a list
cars = ['bmw','audi','toyota','subaru']
print(len(cars))

