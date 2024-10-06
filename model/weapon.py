class Weapon:
    def __init__(self, key, level, ascension, refinement, location, lock, id):
        self.key = key
        self.level = level
        self.ascension = ascension
        self.refinement = refinement
        self.location = location
        self.lock = lock
        self.id = id

    def toJson(self):
        return self.__dict__
