from PIL import ImageGrab, Image
import time

grab = ImageGrab.grab(bbox=(500, 300, 1800, 1000))  # x1,y1,x2,y2
grab.save("grab.png")
time.sleep(3)

img = Image.open("grab.png")
img.show()
