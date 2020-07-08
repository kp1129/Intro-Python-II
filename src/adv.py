from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

    user_choice = input('Where would you like to go from here? n/s/e/w: ')

    if user_choice == 'q':
        print('Thanks for playing!')
        is_playing = False
    elif user_choice == 'n':
        if type(current_room.n_to) is Room:
                current_room = current_room.n_to
                new_player.current_room = current_room.name
                print(f'You are now in the {current_room.name}. {current_room.description}')
        else:
            print('Sorry, you cannot go there. Pick another direction.')        
    elif user_choice == 's':
        if type(current_room.s_to) is Room:
                current_room = current_room.s_to
                new_player.current_room = current_room.name
                print(f'You are now in the {current_room.name}. {current_room.description}')
        else:
            print('Sorry, you cannot go there. Pick another direction.') 
    elif user_choice == 'e':
        if type(current_room.e_to) is Room:
                current_room = current_room.e_to
                new_player.current_room = current_room.name
                print(f'You are now in the {current_room.name}. {current_room.description}')
        else:
            print('Sorry, you cannot go there. Pick another direction.')                   
    elif user_choice == 'w':
        if type(current_room.w_to) is Room:
                current_room = current_room.w_to
                new_player.current_room = current_room.name
                print(f'You are now in the {current_room.name}. {current_room.description}')
        else:
            print('Sorry, you cannot go there. Pick another direction.')         
