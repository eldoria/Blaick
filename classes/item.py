from db_parameters import String, Integer, Column, insert_data_without_duplicates, Base
from sqlalchemy.orm import declared_attr


class Item(Base):
    __tablename__ = 'items'
    id_item = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    type = Column(String)

    def __init__(self, name):
        self.name = name

    __mapper_args__ = {
        'polymorphic_identity': 'item',
        'polymorphic_on': type
    }


class DefensiveItem:
    @declared_attr
    def physical_defense(cls):
        return Item.__table__.c.get('physical_defense', Column(Integer))

    @declared_attr
    def magic_defense(cls):
        return Item.__table__.c.get('magic_defense', Column(Integer))

    @declared_attr
    def weight(cls):
        return Item.__table__.c.get('weight', Column(Integer))


class OffensiveItem:
    @declared_attr
    def power(cls):
        return Item.__table__.c.get('power', Column(Integer))

    @declared_attr
    def weight(cls):
        return Item.__table__.c.get('weight', Column(Integer))


class Head(Item, DefensiveItem):
    def __init__(self, name, physical_defense, magic_defense, weight):
        super().__init__(name)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.weight = weight
        insert_data_without_duplicates(self, Head, Head.name, name)

    __mapper_args__ = {
        'polymorphic_identity': 'head'
    }


class Chest(Item, DefensiveItem):
    def __init__(self, name, physical_defense, magic_defense, weight):
        super().__init__(name)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.weight = weight
        insert_data_without_duplicates(self, Chest, Chest.name, name)

    __mapper_args__ = {
        'polymorphic_identity': 'chest'
    }


class Gloves(Item, DefensiveItem):
    def __init__(self, name, physical_defense, magic_defense, weight):
        super().__init__(name)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.weight = weight
        insert_data_without_duplicates(self, Gloves, Gloves.name, name)

    __mapper_args__ = {
        'polymorphic_identity': 'gloves'
    }


class Pants(Item, DefensiveItem):
    def __init__(self, name, physical_defense, magic_defense, weight):
        super().__init__(name)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.weight = weight
        insert_data_without_duplicates(self, Pants, Pants.name, name)

    __mapper_args__ = {
        'polymorphic_identity': 'pants'
    }


class Boots(Item, DefensiveItem):
    def __init__(self, name, physical_defense, magic_defense, weight):
        super().__init__(name)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.weight = weight
        insert_data_without_duplicates(self, Boots, Boots.name, name)

    __mapper_args__ = {
        'polymorphic_identity': 'boots'
    }


class OffensiveWeapon(Item, OffensiveItem):
    def __init__(self, name, power, weight):
        super().__init__(name)
        self.power = power
        self.weight = weight
        insert_data_without_duplicates(self, OffensiveWeapon, OffensiveWeapon.name, name)

    __mapper_args__ = {
        'polymorphic_identity': 'offensive_weapon'
    }


class DefensiveWeapon(Item, DefensiveItem):
    def __init__(self, name, physical_defense, magic_defense, weight):
        super().__init__(name)
        self.physical_defense = physical_defense
        self.magic_defense = magic_defense
        self.weight = weight
        insert_data_without_duplicates(self, DefensiveWeapon, DefensiveWeapon.name, name)

    __mapper_args__ = {
        'polymorphic_identity': 'defensive_weapon'
    }

'''
class Benediction(Item):
    id_item = Column(String, primary_key=True)
    physical_defense = Column(Integer)
    magic_defense = Column(Integer)
    weight = Column(Integer)

    def __init__(self, id_item, name):
        super().__init__(id_item, name)
        self.id_item = id_item

        # comme dans omniscient reader, ya des constellations sponsors, plus on décide d'attendre d'en prendre une,
        # plus celles-ci deviennent rares (et puissantes)

    __mapper_args__ = {
        'polymorphic_identity': 'benediction'
    }
'''

if __name__ == '__main__':
    head_item = Head('chapeau en cuir', 2, 2, 1)
