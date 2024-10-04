import easyocr
import pandas as pd

reader = easyocr.Reader(["en"], gpu=True)
result = reader.readtext("SPOILER_image.jpg")
result = pd.DataFrame(result)

print(result)
