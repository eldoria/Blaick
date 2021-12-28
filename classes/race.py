from db_parameters import String, Integer, Column, insert_data, Base
from sqlalchemy.orm import declared_attr


class Race(Base):
    __tablename__ = 'race'
    id_session = Column(Integer, primary_key=True, autoincrement=False)
    id_discord = Column(String, primary_key=True, autoincrement=False)
    stamina = Column(Integer)
    gold = Column(Integer)
    weight = Column(Integer)
    health = Column(Integer)
    force = Column(Integer)
    defense = Column(Integer)
    magic_resist = Column(Integer)
    race = Column(String)

    def __init__(self, id_session, id_discord, stamina, gold, weight, health, force, defense, magic_resist):
        self.id_session = id_session
        self.id_discord = id_discord
        self.stamina = stamina
        self.gold = gold
        self.weight = weight
        self.health = health
        self.force = force
        self.defense = defense
        self.magic_resist = magic_resist
        insert_data(self)

    __mapper_args__ = {
        'polymorphic_identity': 'race',
        'polymorphic_on': race
    }


class Human(Race):
    def __init__(self, id_discord, id_session):
        super().__init__(id_discord, id_session, stamina=100, gold=0, weight=60,
                         health=100, force=25, defense=10, magic_resist=5)
    __mapper_args__ = {
        'polymorphic_identity': 'human'
    }


class Elf(Race):
    Column('intelligence', Integer)
    Column('mana', Integer)

    def __init__(self, id_discord, id_session):
        super().__init__(id_discord, id_session, stamina=100, gold=0, weight=50,
                         health=90, force=10, defense=5, magic_resist=15)
        self.intelligence = 20
        self.mana = 50
    __mapper_args__ = {
        'polymorphic_identity': 'elf'
    }


if __name__ == '__main__':
    Human('0000')
