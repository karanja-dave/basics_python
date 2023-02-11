#range function is used to make numerical lists
for value in range(1,11):
    print(value)
#displaying output in a list
numbers = list(range(1,11))
print(numbers)
#skipping numbers
even_numbers = list(range(2,11,2))
print(even_numbers)
#creating any set of numbers ie set of squares metthod1
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
#method 2
squares = []
for value in range(1,11):
    squares =(value**2)
    print(squares)
#list comprehension method3
squares = [value**2 for value in range(1,11)]
print(squares)   
#STATISTICS
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#A million numbers
numbers=list(range(1,100001))
for number in numbers:
    print(number)