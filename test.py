import pytesseract

from process_image import process_image

img_path = "file (1).png"

processed_img = process_image(img_path)

config = "--oem 1 --psm 6"

ocr_result1 = pytesseract.image_to_string(processed_img, config=config, lang="eng")
print("result 1 =============\n" + ocr_result1)
