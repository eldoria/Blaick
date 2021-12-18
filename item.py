class Item:
    def __init__(self, name):
        self.name = name


class Head(Item):
    def __init__(self, name, physical_defense, magic_defense, weight):
        super().__init__(name)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.weight = weight


class Chest(Item):
    def __init__(self, name, physical_defense, magic_defense, weight):
        super().__init__(name)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.weight = weight


class Gloves(Item):
    def __init__(self, name, physical_defense, magic_defense, weight):
        super().__init__(name)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.weight = weight


class Pants(Item):
    def __init__(self, name, physical_defense, magic_defense, weight):
        super().__init__(name)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.weight = weight


class Boots(Item):
    def __init__(self, name, physical_defense, magic_defense, weight):
        super().__init__(name)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.weight = weight


class OffensiveArm(Item):
    def __init__(self, name, power, weight):
        super().__init__(name)
        self.power = power
        self.weight = weight


class DefensiveArm(Item):
    def __init__(self, name, physical_defense, magic_defense, weight):
        super().__init__(name)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.weight = weight


class Enchantment(Item):
    def __init__(self, name):
        super().__init__(name)
        # Faire des sous-classes enchantements de santé, enchantement magique ...
