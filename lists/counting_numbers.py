#range() and for loops
for value in range(1,21):
    print(value)

#counting a million numbers
million_numbers = range(1,100001)
#for number in million_numbers:
   # print(number)

#statistics   
print(min(million_numbers))
print(max(million_numbers))
print(sum(million_numbers))

#skipping items in list
odd_numbers = range(1,21,2)
for number in odd_numbers:
    print(number)

#multiples of 3
multiples_0f_3 = []
for value in range(3,31):
    multiple_3=value*3
    multiples_0f_3=multiple_3
    print(multiples_0f_3)    

#cube  
cubes=[]
for value in range(1,11):
    cube=value**3
    cubes=cube
    print(cubes)  

#list comprehension
cubes = [value**3 for value in range(1,11)] 
print(cubes)
