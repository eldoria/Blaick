from db_parameters import String, Integer, Boolean, Column, insert_data, Base
from sqlalchemy import ForeignKey


class Inventory(Base):
    __tablename__ = 'inventory'
    id_session = Column(Integer, primary_key=True, autoincrement=False)
    id_discord = Column(String, primary_key=True, autoincrement=False)
    id_item = Column(ForeignKey('items.id_item'))
    quantity = Column(Integer)

    def __init__(self, id_session, id_discord, id_item, quantity):
        self.id_session = id_session
        self.id_discord = id_discord
        self.id_item = id_item
        self.quantity = quantity
        insert_data(self)
