#accessing a character in list,composing message and assign it in a variable
guests = ['jeff','dan','caleb','betty']
message = f"Hello {guests[0].title()}, you're invited to my party"
print(message)
message = f"Hello {guests[1].title()}, you're invited to my party"
print(message)
message = f"Hello {guests[2].title()}, you're invited to my party"
print(message)
message = f"Hello {guests[3].title()}, you're invited to my party"
print(message)
print(f"Unfortunately, {guests[1].title()} won't be attending the party")
#modifying list/changing an item in a list
guests[1] = "dave"
print(guests)
#composing message with new item overwritten in list 
print(f"Hello {guests[0].title()}, you're invited to my party")
print(f"Hello {guests[1].title()}, you're invited to my party")
print(f"Hello {guests[2].title()}, you're invited to my party")
print(f"Hello {guests[3].title()}, you're invited to my party")
print('This iS to inform you that more guests will be joining us at the party')
#add items in a list
guests.insert(0, 'harriet')
guests.insert(2, 'ken')
guests.append('fridah')
print(guests)
print(f"Hello {guests[0].title()}, you're welcomed to my party\n")
print(f"Hello {guests[1].title()}, you're welcomed to my party\n")
print(f"Hello {guests[2].title()}, you're welcomed to my party\n")
print(f"Hello {guests[3].title()}, you're welcomed to my party\n")
print(f"Hello {guests[4].title()}, you're welcomed to my party\n")
print(f"Hello {guests[5].title()}, you're welcomed to my party\n")
print(f"Hello {guests[6].title()}, you're welcomed to my party\n")
#remove items in a list
print("Am sorry to inform you that the party is only compatible for two guests")
print(guests)
#pop()
print(f"{guests.pop().title()}, you're not invited") #remove guests&compose message without variable assignment
print(f"{guests.pop(0).title()}, you're not invited")
print(f"{guests.pop(0).title()}, you're not invited")
print(guests)
#remove()
#remove an item
guests.remove('dave')
print(guests)
#providing a statment
not_invited = 'ken'
guests.remove(not_invited)
print(f"{not_invited.title()}, you're not invited")
#del statment
del guests[0]
del guests[0]
print(guests)