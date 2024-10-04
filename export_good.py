from models.artifact import Artifact, Substat
from models.weapon import Weapon
from models.character import Character, Talent
from models.GOOD import Good

import json


good = Good(
    [Character("Gaming", 60, 1, 4, Talent(1, 6, 6))],
    [
        Artifact(
            "TenacityOfTheMillelith",
            "flower",
            20,
            5,
            "hp",
            "Gaming",
            True,
            [
                Substat("critDMG_", 13.2),
                Substat("hp_", 4.1),
                Substat("eleMas", 35),
                Substat("critRate_", 11.3),
            ],
            0,
        ),
        Artifact(
            "HeartOfDepth",
            "plume",
            20,
            5,
            "atk",
            "Gaming",
            True,
            [
                Substat("def", 39),
                Substat("critRate_", 13.2),
                Substat("critDMG_", 14.0),
                Substat("hp", 269),
            ],
            1,
        ),
        Artifact(
            "CrimsonWitchOfFlames",
            "sands",
            20,
            5,
            "atk_",
            "Gaming",
            True,
            [
                Substat("atk", 37),
                Substat("hp", 209),
                Substat("critDMG_", 7.8),
                Substat("critRate_", 14.8),
            ],
            2,
        ),
        Artifact(
            "UnfinishedReverie",
            "goblet",
            20,
            5,
            "pyro_dmg_",
            "Gaming",
            True,
            [
                Substat("critRate_", 3.1),
                Substat("atk", 37),
                Substat("eleMas", 47),
                Substat("atk_", 14.0),
            ],
            3,
        ),
        Artifact(
            "FragmentOfHarmonicWhimsy",
            "circlet",
            20,
            5,
            "critDMG_",
            "Gaming",
            False,
            [
                Substat("hp_", 8.7),
                Substat("critRate_", 7.0),
                Substat("hp", 837),
                Substat("atk", 14),
            ],
            4,
        ),
    ],
    [Weapon("FangOfTheMountainKing", 80, 5, 1, "Gaming", True, 0)],
)

file = open("genshin_data/export.json", "x")

x = good.toJson()
file.write(json.dumps(x))
file.close()
