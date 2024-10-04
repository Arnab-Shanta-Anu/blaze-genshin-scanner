from PIL import ImageGrab
import time

waitTime = 3


# size 490x780
def take_screen_shot():
    take_weapon_screen_shot()


def take_artifact_screen_shot():
    time.sleep(waitTime)
    grab = ImageGrab.grab(bbox=(1320, 180, 1790, 960))  # x1,y1,x2,y2
    grab.save("grab.png")


def take_weapon_screen_shot():
    time.sleep(waitTime)
    grab = ImageGrab.grab(bbox=(1320, 130, 1790, 960))  # x1,y1,x2,y2
    grab.save("grab.png")


def take_char_screen_shot():
    pass


take_screen_shot()
