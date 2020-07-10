# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def get(self, item):
        self.items.append(item)        
        print(f'\nYou picked up the {item.name}! Use it wisely.')
        return True

    def drop(self, item):
        has_item = False
        for i in self.items:
            if i.name == item:
                self.items.remove(i)
                has_item = True
                print(f"\nYou stashed the {item} in this room. Remember this for later.")
                return i
        if not has_item:
            print("\nHmm, you don't have this item on you.")  

    def hit_a_wall(self):
        print('\nSorry, you cannot go there. Pick another direction.')    

    def display_items(self):
        print('\nYou are carrying the following items:\n')
        for item in self.items:
            print(f"{item.name}")
