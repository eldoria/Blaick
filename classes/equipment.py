from db_parameters import String, Integer, Column, insert_data, Base
from sqlalchemy import ForeignKey


class Equipment(Base):
    __tablename__ = 'inventory'
    id_session = Column(Integer, primary_key=True, autoincrement=False)
    id_discord = Column(String, primary_key=True, autoincrement=False)
    id_item = Column(ForeignKey('inventory.id_item'))

    def __init__(self, id_session, id_discord, id_item):
        self.id_session = id_session
        self.id_discord = id_discord
        self.id_item = id_item
        insert_data(self)
