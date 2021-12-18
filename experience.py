class Experience:
    def __init__(self):
        self.level = 1
        self.experience = 0
        self.experience_required = 10

    def gain_experience(self, amount):
        print(f"nom_joueur gagne {amount} experiences")
        self.experience += amount
        self.check_level_up()

    def level_up(self):
        self.level += 1
        print(f"nom_joueur passe niveau {self.level}")
        extra_experience = self.experience - self.experience_required
        self.experience_required *= 1.15
        self.experience = extra_experience
        self.check_level_up()

    def check_level_up(self):
        if self.experience >= self.experience_required:
            self.level_up()

# x 1.1
# 1000 xp -> niv 26
# 10000 xp -> niv 49
# 100000 xp -> niv 73
# 1000000 xp -> niv 97
# 10000000 xp -> niv 121

# x 1.15
# 1000 xp -> niv 20
# 10000 xp -> niv 36
# 100000 xp -> niv 53
# 1000000 xp -> niv 69
# 10000000 xp -> niv 86
