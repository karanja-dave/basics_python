#if-elif-else -tests atleast 2situations
#original approach of if-elif-else statments
age=12
if age<4:
    print("Your admission cost is ksh.00\n")
elif age<18:
    print("Your admission cost is ksh.2500\n")
else:
    print("Your admission cost is ksh.4000\n")
#if=elif-else chain approach
age=12
if age<4:
    cost=00
elif age<18:
    cost=2500
else:
    cost=4000
print(f"Your admission cost is ksh.{cost}\n")
#using multiple eilif blocks
age=12
if age<4:
    cost=00
elif age<18:
    cost=2500
elif age<65:
    cost=4000
else:
    cost=2000
print(f"Your admission cost is ksh.{cost}\n")
#omitting the else block
age=12
if age<4:
    cost=00
elif age<18:
    cost=2500
elif age<65:
    cost=4000
elif age>=65:
    cost=2000
print(f"Your admission cost is ksh.{cost}\n")

