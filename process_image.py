import time
import cv2
import numpy as np


def process_image(img):
    img = cv2.imread(img)
    return noise_reduction(binarize(gray_scale(img)))


def gray_scale(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("temp/grayscale.png", gray_img)
    time.sleep(3)
    return gray_img


def binarize(img):
    threshold, bw_img = cv2.threshold(img, 200, 230, cv2.THRESH_BINARY)
    cv2.imwrite("temp/bwimage.png", bw_img)
    time.sleep(3)
    return bw_img


def noise_reduction(img):
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    img = cv2.medianBlur(img, 3)

    cv2.imwrite("temp/noise_reduced.png", img)
    return img
