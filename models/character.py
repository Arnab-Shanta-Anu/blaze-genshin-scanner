class Character:
    def __init__(self, key, level, constellation, ascension, talent):
        self.key = key
        self.level = level
        self.constellation = constellation
        self.ascension = ascension
        self.talent = talent

    def toJson(self):
        self.talent = self.talent.toJson()

        return self.__dict__


class Talent:
    def __init__(self, auto, skill, burst):
        self.auto = auto
        self.skill = skill
        self.burst = burst

    def toJson(self):
        return self.__dict__
