from db_parameters import String, Integer, Column, insert_data, Base
from sqlalchemy import ForeignKey


class Market(Base):
    __tablename__ = 'market'
    id_session = Column(Integer, primary_key=True, autoincrement=False)
    id_discord = Column(String, primary_key=True, autoincrement=False)
    id_item = Column(ForeignKey('inventory.id_item'))
    type = Column(String)
    gold = Column(Integer)

    def __init__(self, id_session, id_discord, id_item, type, gold):
        self.id_session = id_session
        self.id_discord = id_discord
        self.id_item = id_item
        self.type = type
        self.gold = gold
        insert_data(self)
