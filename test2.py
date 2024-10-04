import os
import easyocr
import pandas as pd
# from models.artifact import Artifact

reader = easyocr.Reader(["en"], gpu=True)

# imageFilePath = "images/"
# exportFilePath = "./genshin_data/"

# for imageFile in os.listdir(imageFilePath):
#     result = reader.readtext(imageFilePath + imageFile)
#     texts = ""
#     for bbox, text, conf in result:
#         texts = texts + text

#     file = open("./genshin_data/export.txt", "a")
#     file.write(texts)
#     file.close()

result = reader.readtext("grab.png")
print(pd.DataFrame(result, columns=["bbox", "text", "pred"]))
