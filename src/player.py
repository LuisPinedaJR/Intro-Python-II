class Player:
    def __init__(self, current_room, inventory):
        self.current_room = current_room
        self.inventory = inventory
    
    def get_item(self, item):
        self.inventory.append(item)
        self.current_room.items.remove(item)

    
    def drop_item(self, item):
        self.current_room.items.append(item)
        self.inventory.remove(item)