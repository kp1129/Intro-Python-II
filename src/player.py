# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def drop(self, item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)
                print(f"You stashed the {item} in this room. Remember this for later.")
            