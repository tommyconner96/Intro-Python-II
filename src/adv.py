from room import Room
from player import Player
from item import Item
from room import RoomItems

# Declare all items
item_knife = Item('knife', 'a small knife')
item_lamp = Item('lamp', 'old brass lamp')
item_watch = Item('watch', 'a pocket watch')
item_lighter = Item('lighter', 'a cigarette lighter')

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     item_knife),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    item_watch),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                    item_lighter),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    item_lamp),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                    None),
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

# acceptable direction inputs
north = ['N', 'NORTH']
south = ['S', 'SOUTH']
east = ['E', 'EAST']
west = ['W', 'WEST']

# Make a new player object that is currently in the 'outside' room.
newPlayer = Player(input("Please input your name:\n"), room['outside'])

print(f"Hello, {newPlayer.name}!")
while True:
    current_room = newPlayer.current_room
    # * Prints the current room name
    print(f"{newPlayer.current_room.name}")
    # * Prints the current description (the textwrap module might be useful here).
    print(f"{newPlayer.current_room.description}")
    if current_room.item is not None:
        print(f"There is a {current_room.item[0].name} in this room.\n")
    # * Waits for user input and decides what to do.
    move = input("Enter your next move or press Q to quit:\n")
    # If the user enters "q", quit the game.
    if move.upper() == 'Q':
        break
    # Or if they enter quit, just for user-friendliness sake
    elif move.upper() == 'QUIT':
        break
    # If the user enters a cardinal direction, attempt to move to the room there.
    elif move.upper() in north:
        if hasattr(current_room, "n_to"):
            if current_room.n_to is not None:
                newPlayer.current_room = getattr(current_room, "n_to")
            else:
                print("You cannot go North from here!")
    elif move.upper() in south:
        if hasattr(current_room, "s_to"):
            if current_room.s_to is not None:
                newPlayer.current_room = getattr(current_room, "s_to")
            else:
                print("You cannot go South from here!")
    elif move.upper() in east:
        if hasattr(current_room, "e_to"):
            if current_room.e_to is not None:
                newPlayer.current_room = getattr(current_room, "e_to")
            else:
                print("You cannot go East from here!")
    elif move.upper() in west:
        if hasattr(current_room, "w_to"):
            if current_room.w_to is not None:
                newPlayer.current_room = getattr(current_room, "w_to")
            else:
                print("You cannot go West from here!")
    else:
        print("That is an invalid command")
        pass
