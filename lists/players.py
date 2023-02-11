#slicing in lists 
players = ['charles','martina','michael','florence','eli']
print(players[0:3])
#slice the 1st elements upto the last element you want to work with
print(players[:4])
#slicing the 1st items at the end of the list upto the last one ypu want to work with
print(players[-2:])
#slicing and skipping items in a list
print(players[0:5:2])

#looping through a slice
print("\nHere's the list of my first four players:")
for player in players[:4]:
    print(player.title())
#copying a list
print("These are my favourite players:")
print(players)
print("\nThese are my friend's favourite players: ")
friends_players = players[:]
print(friends_players)
#adding differrent items on the independent lists
players.append('diego')
friends_players.append('luther')
print(players)
print(friends_players)