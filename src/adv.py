
from room import Room
from player import Player
# Declare all the rooms

outside = Room("Outside Cave Entrance",
                "North of you, the cave mount beckons"""),

foyer = Room("Foyer", """Dim light filters in from the south. Dusty
                passages run north and east."""),

overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
                into the darkness. Ahead to the north, a light flickers in
                the distance, but there is no way across the chasm."""),

narrow = Room("Narrow Passage", """The narrow passage bends here from west
                to north. The smell of gold permeates the air."""),

treasure = Room("Treasure Chamber", """You've found the long-lost treasure
                chamber! Sadly, it has already been completely emptied by
                earlier adventurers. The only exit is to the south.""")


# Link rooms together

outside.n_to = foyer
foyer.s_to = outside
foyer.n_to = overlook
foyer.e_to = narrow
overlook.s_to = foyer
narrow.w_to = foyer
narrow.n_to = treasure
treasure.s_to = narrow

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player()
player.current_room = outside
while True:
# Write a loop that:

    # * Prints the current room name
    print(player.current_room)
    # * Prints the current description (the textwrap module might be useful 
    # here).
    print(player.current_room.description)

    # * Waits for user input and decides what to do.
    input_var = input('Enter next move')
    #
    # If the user enters a cardinal direction, attempt to move to the room 
    # there.
    if input_var == 'n':
        # check if current room has a n_to attribute
        
        if hasattr(player.current_room, f'{input_var}_to'):
            
            # move player to that room
            
            player.current_room = getattr(player.current_room, f'{input_var}_to')
            
                
            
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
