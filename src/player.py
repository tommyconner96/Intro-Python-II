from room import Room

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room: Room = current_room
        self.inventory = []
