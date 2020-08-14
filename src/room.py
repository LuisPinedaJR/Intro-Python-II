# Implement a class to hold room information. This should have name and
# description attributes.

from player import Player

class Room(Player):
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items