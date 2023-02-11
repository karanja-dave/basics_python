#tuples
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])
#making a tuple with one element
ty_h = (3,)
print(ty_h)
#looping through all values of a tuple
for dimension in dimensions:
    print(dimension)
    #writing over a tuple/modifying a tuple
print("\nHere's the original dimensions:")
for dimension in dimensions[:2]:
    print(dimension)
dimensions = (400,100)
print("\nHere's the modified dimensions:")
for dimension in dimensions:
    print(dimension)

