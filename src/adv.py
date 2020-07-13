from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons.", None),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item("map", "The Migrating Moon Map is infused with powerful magic\nthat can lead you to whatever it is that your heart desires...\nNo matter where in the universe it is.")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item("sword",
                "The magical Elven Sword makes its bearer impossible to defeat.\nYour enemies are already trembling in their boots...")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item("scroll", "Ah, the Ancient Scroll of Forbidden Mysteries written\nby the exiled elven mages in the world before.\nYou will never sleep again...")),

    'treasure': Room("Treasure Chamber", """You've found it!\nSadly, it has already been completely emptied by earlier adventurers.\nThe only exit is to the south.""", None),
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

# set up new player
player_name = input('Welcome! Please choose a name for your character: ')
new_player = Player(player_name, 'Outside Cave Entrance')
is_playing = True
# set up starting location
current_room = room['outside']
print(f'\n{new_player.name}, you are standing in front of the {current_room.name}. '
        + f'You take some time to look around.\n{current_room.description}')

while is_playing:
    
    user_choice = input('\nWhere would you like to go from here?\n[n] [s] [e] [w] to move'
                        + '\n[get] and [drop] to pick up/drop loot\nor [q] to quit: ')

    if user_choice == 'q':
        print('\nThanks for playing!\n')
        is_playing = False

    elif user_choice == 'get':
        if len(current_room.items) > 0 and current_room.items[0] != None:
            current_room.display_items()
            item_to_get = input('\nName of item you want to pick up: ')
            item_picked_up = False
            for item in current_room.items:
                if item.name == item_to_get.lower():
                    item_picked_up = new_player.get(item)
                    current_room.items.remove(item)
            if not item_picked_up:
                print('\nOops! Looks like there is no such item here')
        else:
            print('\nThis room has no loot :(')
            
    elif user_choice == 'drop':
        if len(new_player.items) > 0:
            new_player.display_items()
            item_to_drop = input('\nName of item you want to stash in this room: ')
            item_dropped = new_player.drop(item_to_drop.lower())
            if item_dropped:
                current_room.items.append(item_dropped)
        else:
            print("\nYou have no items.")           

    elif user_choice == 'n':
        if type(current_room.n_to) is Room:
                current_room = current_room.n_to
                new_player.current_room = current_room.name
                current_room.explore()   
        else:
            new_player.hit_a_wall()        
    elif user_choice == 's':
        if type(current_room.s_to) is Room:
                current_room = current_room.s_to
                new_player.current_room = current_room.name
                current_room.explore()
        else:
            new_player.hit_a_wall() 
    elif user_choice == 'e':
        if type(current_room.e_to) is Room:
                current_room = current_room.e_to
                new_player.current_room = current_room.name
                current_room.explore()
        else:
            new_player.hit_a_wall()                   
    elif user_choice == 'w':
        if type(current_room.w_to) is Room:
                current_room = current_room.w_to
                new_player.current_room = current_room.name
                current_room.explore()
        else:
            new_player.hit_a_wall()         
