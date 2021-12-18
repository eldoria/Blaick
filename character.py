from stats import Stats
from item import Item
from experience import Experience


class Character:
    def __init__(self,
                 name,
                 ):
        self.name = name
        self.stats = Stats(health=10, force=10, defense=10, magic_resist=10)
        self.items = [Item] * 9
        self.experience = Experience
