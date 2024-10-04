import os
import string
import easyocr
import pandas as pd

from consts.artifact_consts import ARTIFACTSLOTKEYS, allMainStatKeys
from models.artifact import Artifact, Substat
# from models.artifact import Artifact

reader = easyocr.Reader(["en"], gpu=True)

imageFilePath = "images/"
exportFilePath = "./genshin_data/export.txt"

texts = []

for imageFile in os.listdir(imageFilePath):
    artifact = Artifact()
    substats = {}

    result = reader.readtext(imageFilePath + imageFile)

    #########################################################
    # first 9 line gives details about setKey,mainStat,     #
    # subStats and setKey                                   #
    # then skip to end to find the equipped char            #
    #########################################################

    for index, (bbox, text, conf) in enumerate(result):
        if index == 0:
            # ### getting the piece ###################
            text = text.split(" ")[0].lower()
            if text in ARTIFACTSLOTKEYS:
                texts.append("slotKey = " + text)
                artifact.slotKey = text

        elif index == 1:
            # ### getting the main stat ##############
            if text in allMainStatKeys:
                texts.append("Main stat = " + allMainStatKeys[text])
                artifact.mainStatKey = allMainStatKeys[text]

        elif index == 2:
            pass

        elif index == 3:
            # ### getting the level ##############
            text = text.replace("+", "")
            texts.append("level = " + text)
            artifact.level = text

        ################TODO:#######################
        #      this only covers 4 substat          #
        ############################################

        elif index in range(4, 8):
            # ### getting sub stats ##################
            key, value = text.split("+")

            if "%" in value:
                key = key + "_"
                value = value.replace("%", "")

            if key in allMainStatKeys:
                key = allMainStatKeys[key]

            value = float(value)
            texts.append(key + " " + str(value))
            substat = Substat(key, value)
            substats[key] = value

        elif index == 8:
            # ### getting the set ####################
            text = text.replace(":", "")
            text = string.capwords(text).replace(" ", "")
            texts.append("setKey = " + text)
            artifact.setKey = text

        elif "Equipped:" in text:
            texts.append("location = " + text.split(" ")[1])
            artifact.location = text.split(" ")[1]

    artifact.substats = substats
    texts.append("==============================")
    # print(artifact.toJson())

with open(exportFilePath, "w") as file:
    for item in texts:
        file.write(f"{item}\n")
    print("strings written to file\nexitting.....")

# result = reader.readtext("grab.png")
# print(pd.DataFrame(result, columns=["bbox", "text", "pred"]))
