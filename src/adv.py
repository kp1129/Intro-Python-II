from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", None),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item("map", "Migrating Moon Map is infused with powerful magic that can lead you to whatever it is that your heart desires...no matter where in the universe it is.")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("sword",
                "The magical Elven Sword makes its bearer impossible to defeat.")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item("scroll", "Ancient Scroll of Mysteries written by the exiled elven mages in the world before.")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", None),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# declare all the items

# item = {
#     'sword': Item("Elven Sword",
#                 "A magical elven sword that makes its bearer impossible to defeat"),
#     'scroll': Item("Scroll of Mysteries", "An ancient scroll written by the exiled elven mages in the world before"),
#     'map': Item("Migrating Moon Map", "A map infused with powerful magic that can lead you to whatever it is that your heart desires...no matter where in the universe it is")            
# }

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


player_name = input('Welcome! Please choose a name for your character: ')
new_player = Player(player_name, 'Outside Cave Entrance')
current_room = room['outside']
is_playing = True

print(f'{new_player.name}, you are standing in front of the {current_room.name}. You take some time to look around. {current_room.description}')

while is_playing:

    user_choice = input('Where would you like to go from here? [n] [s] [e] [w]: ')

    if user_choice == 'q':
        print('Thanks for playing!')
        is_playing = False

    elif user_choice == 'get':
        if len(current_room.items) > 0:
            new_player.items.append(current_room.items[0])
            del current_room.items[0]
            new_item = new_player.items[-1]
            print(f"You picked up a {new_item}. Use it wisely.")
            
    elif user_choice == 'drop':
        if len(new_player.items) > 0:
            print('You are carrying the following items:')
            for item in new_player.items:
                print(item.name)
            item_to_drop = input('Which item do you want to stash in this room: ')
            item_dropped = False
            for item in new_player.items:
                if item.name == item_to_drop.lower():
                    new_player.drop(item_to_drop.lower())
                    current_room.items.append(item)
                    item_dropped = True
            if not item_dropped:
                print("Hmm, you don't have this item on you.")    
        else:
            print("You have no items. Try exploring more rooms.")           

    elif user_choice == 'n':
        if type(current_room.n_to) is Room:
                current_room = current_room.n_to
                new_player.current_room = current_room.name
                print(f'You are now in the {current_room.name}. {current_room.description}')
                if len(current_room.items) > 0 and current_room.items[0] != None:
                    print("This room contains the following items: ")
                    for item in current_room.items:
                        print(f"Item: {item.name}: {item.description}")
                    print("To pick up an item, enter [get ITEM]")    
        else:
            print('Sorry, you cannot go there. Pick another direction.')        
    elif user_choice == 's':
        if type(current_room.s_to) is Room:
                current_room = current_room.s_to
                new_player.current_room = current_room.name
                print(f'You are now in the {current_room.name}. {current_room.description}')
                if len(current_room.items) > 0 and current_room.items[0] != None:
                    print("This room contains the following items: ")
                    for item in current_room.items:
                        print(item)
        else:
            print('Sorry, you cannot go there. Pick another direction.') 
    elif user_choice == 'e':
        if type(current_room.e_to) is Room:
                current_room = current_room.e_to
                new_player.current_room = current_room.name
                print(f'You are now in the {current_room.name}. {current_room.description}')
                if len(current_room.items) > 0 and current_room.items[0] != None:
                    print("This room contains the following items: ")
                    for item in current_room.items:
                        print(item)
        else:
            print('Sorry, you cannot go there. Pick another direction.')                   
    elif user_choice == 'w':
        if type(current_room.w_to) is Room:
                current_room = current_room.w_to
                new_player.current_room = current_room.name
                print(f'You are now in the {current_room.name}. {current_room.description}')
                if len(current_room.items) > 0 and current_room.items[0] != None:
                    print("This room contains the following items: ")
                    for item in current_room.items:
                        print(item)
        else:
            print('Sorry, you cannot go there. Pick another direction.')         
