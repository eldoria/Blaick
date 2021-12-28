from db_parameters import String, Integer, Column, Base, insert_data


# Il peut y a plusieurs sessions de jeux simultanée
class Session(Base):
    __tablename__ = 'session'
    id_session = Column(Integer, primary_key=True, autoincrement=False)
    id_discord = Column(String, primary_key=True, autoincrement=False)

    def __init__(self, id_session, id_discord):
        self.id_session = id_session
        self.id_discord = id_discord
        insert_data(self)

