from db_parameters import String, Integer, Column, insert_data, Base


class Experience(Base):
    __tablename__ = 'experience'
    id_session = Column(Integer, primary_key=True, autoincrement=False)
    id_discord = Column(String, primary_key=True, autoincrement=False)
    level = Column(Integer)
    experience = Column(Integer)
    experience_required = Column(Integer)

    def __init__(self, id_session, id_discord):
        self.id_session = id_session
        self.id_discord = id_discord
        self.level = 1
        self.experience = 0
        self.experience_required = 10
        insert_data(self)

    def gain_experience(self, amount):
        print(f"nom_joueur gagne {amount} experiences")
        self.experience += amount
        self.check_level_up()

    def level_up(self):
        self.level += 1
        print(f"nom_joueur passe niveau {self.level}")
        extra_experience = self.experience - self.experience_required
        self.experience_required *= 10
        self.experience = extra_experience
        self.check_level_up()

    def check_level_up(self):
        if self.experience >= self.experience_required:
            self.level_up()


# create_table = "CREATE TABLE IF NOT EXISTS experience (id_discord text, \
#                                                       level integer, \
#                                                      experience integer, \
#                                                       experience_required integer)"

# delete_table = "DROP TABLE experience"


if __name__ == "__main__":
    # create_table(table_experience)
    # delete_table(table_experience)
    # exp = Experience('00000')
    exp = Experience('23073')

# J'ai changé d'avis, je veut faire un jeu avec très peu de niveaux et ou ceci apportent des avantages conséquents

