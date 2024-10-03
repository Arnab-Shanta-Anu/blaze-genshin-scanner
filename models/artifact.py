class Artifact:
    def __init__(
        self, setKey, slotKey, level, rarity, mainStatKey, location, lock, substats, id
    ) -> None:
        self.setKey = setKey
        self.slotKey = slotKey
        self.level = level
        self.rarity = rarity
        self.mainStatKey = mainStatKey
        self.location = location
        self.lock = lock
        self.substats = substats
        self.id = id

    def toJson(self):
        substats = []
        for substat in self.substats:
            substats.append(substat.toJson())

        self.substats = substats

        return self.__dict__


class Substat:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value

    def toJson(self):
        return self.__dict__
