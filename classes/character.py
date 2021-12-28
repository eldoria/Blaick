from classes.session import Session
from classes.race import Human
from classes.experience import Experience


class Character:
    def __init__(self, id_session: int, id_discord: str):
        Session(id_session, id_discord)
        Human(id_session=id_session, id_discord=id_discord)
        Experience(id_session=id_session, id_discord=id_discord)
