class Room:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.item = item
        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None
