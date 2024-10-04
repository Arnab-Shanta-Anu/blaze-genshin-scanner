class Good:
    def __init__(self, characters, artifacts, weapons):
        self.format = "GOOD"
        self.source = "blaze genshin scanner"
        self.version = 1
        self.characters = characters
        self.artifacts = artifacts
        self.weapons = weapons

    def toJson(self):
        characters = []
        for character in self.characters:
            characters.append(character.toJson())
        self.characters = characters

        artifacts = []
        for artifact in self.artifacts:
            artifacts.append(artifact.toJson())
        self.artifacts = artifacts

        weapons = []
        for weapon in self.weapons:
            weapons.append(weapon.toJson())
        self.weapons = weapons

        return self.__dict__
