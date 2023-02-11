#tupules
foods=('vegetable','meat','beans','sauces','peanut')
for food in foods:
    print(food.title())
#foods[0]='green grams' a modified code-wont work-cant modify loops directly
#modify a tupule
print("\nOriginal tupule list:")
for food in foods:
    print(food.title())

foods=('fruits','mutton','beans','sauces','peanut')
print("\nModified tuple list:")
for food in foods:
    print(food.title())