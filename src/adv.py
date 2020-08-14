from room import Room
from player import Player

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["key"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm.""", ["knife"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
    to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south.""", []),
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
player = Player(room['outside'], [])

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

while True:

    current_room = player.current_room
    inventory = player.inventory
    room_items = Room(current_room.name, current_room.description, current_room.items).items
    # print(room_items, ' is room items!!!')
   
    print(f" \n You are in the {current_room.name}")
    print(current_room.description)
    print(f"Things in this room: {room_items}")
    print(f"\n Your inventory: {player.inventory}")

    decision = input(" \n Where would you like to do? ")

    if decision == 'help':
        print(" \n Pick a direction to travel: n, e, s, w \n Or get [item name] drop [item name] \n or q to quit")
    elif decision ==  'n':
        print("You head north")
        try:
           player = Player(current_room.n_to, inventory)
        except AttributeError:
            print(" \n YOU CANNOT GO NORTH. \n")
            print("Please pick a different direction. \n")

    elif decision == 's':
        print("You head south.")
        try:
            player = Player(current_room.s_to, inventory)
        except AttributeError:
            print(" \n YOU CANNOT GO SOUTH. \n")
            print("Please pick a different direction. \n")

    elif decision == 'e':
        print("You head east.")
        try:
            player = Player(current_room.e_to, inventory)
        except AttributeError:
            print(" \n YOU CANNOT GO EAST. \n")
            print("Please pick a different direction. \n")

    elif decision == 'w':
        print("You head west.")
        try:
            player = Player(current_room.w_to, inventory)
        except AttributeError:
            print(" \n YOU CANNOT GO WEST. \n")
            print("Please pick a different direction. \n")

    elif decision == 'q':
        quit()

    for item in room_items:
        if decision == f"get {item}":
            print(f"\n You pick up the {item}")
            player.get_item(item)
    
    for item in player.inventory:
          if decision == f"drop {item}":
            print(f"\n You drop the {item}")
            player.drop_item(item)