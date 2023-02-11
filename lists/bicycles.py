#lists
bicycles = ['trek','cannondale','redline','specializzed']
print(bicycles)
#access individual items
print(bicycles[0])#index 0 rep 1st item on a list
#access multiple items
print(bicycles[1])
print(bicycles[2])
#access last item
print(bicycles[-1])
#edditing items to give neat output-techniques of last chapter
print(bicycles[3].title())
#compose messages using items in list
message = f"my first bicycle was a {bicycles[2].title()}"
print(message)