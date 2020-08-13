class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None

# # Make a new player object that is currently in the 'outside' room.
# player1 = Player1(room['outside'])
# player2 = Player2('outside')
# # Write a loop that:
# #
# while True:
# # * Prints the current room name
#     current_room = player1.current_room
#     print("player1", player1.current_room.name)
#     print("player2", room[player2.current_room].name)
# # * Prints the current description (the textwrap module might be useful here).
#     print(player1.current_room.description)
# # * Waits for user input and decides what to do.
#     user_input = input("Choose a direction to move in ('n', 's', 'e', 'w'):\n")
# # If the user enters a cardinal direction, attempt to move to the room there.
#     if user_input == "n":
#         if hasattr(current_room, "n_to"): 
#         # if current_room.n_to is not None:
#             player1.current_room = getattr(current_room, "n_to")
#             player1.current_room = current_room.n_to
#         else: 
#             # handle error
#             pass
#     # You can dynamically generate attributes like on the line below and then check/access them using hasattr and getattr 
#     attribute = user_input + "_to"
# # Print an error message if the movement isn't allowed.
# #
# # If the user enters "q", quit the game.