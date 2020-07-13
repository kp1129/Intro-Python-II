# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, item):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = [item]

    def explore(self):
        print(f"\nYou are now in the {self.name}. {self.description}")
        if len(self.items) > 0 and self.items[0] != None:
            print("\nAnd you see some loot! Let's see what you found:")
            for item in self.items:
                print(f"\nItem: {item.name}\n{item.description}")

    def display_items(self):
        print('\nThis room has the following items:')
        for item in self.items:
            print(f"\nItem: {item.name}\n{item.description}")            