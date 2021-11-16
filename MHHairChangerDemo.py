import cv2
from PIL import Image
import numpy as np


image = cv2.resize(cv2.imread(r"Images\00009.png"), (512, 512))

original_image = image.copy()
mask = cv2.imread(r"Masks\00009_hair.png", 0)

pixels = np.nonzero(mask)


def redTrackbarChanged(x):
    global image
    image[pixels] = np.clip(
        original_image[pixels].astype(np.float) * (1, 1, x / 100), 0, 255
    )
    image = image.astype(np.uint8)


def greenTrackbarChanged(x):
    global image
    image[pixels] = np.clip(
        original_image[pixels].astype(np.float) * (1, x / 100, 1), 0, 255
    )
    image = image.astype(np.uint8)


def blueTrackbarChanged(x):
    global image
    image[pixels] = np.clip(
        original_image[pixels].astype(np.float) * (x / 100, 1, 1), 0, 255
    )
    image = image.astype(np.uint8)


cv2.namedWindow("image")

cv2.createTrackbar("R", "image", 100, 200, redTrackbarChanged)
cv2.createTrackbar("G", "image", 100, 200, greenTrackbarChanged)
cv2.createTrackbar("B", "image", 100, 200, blueTrackbarChanged)

while 1:
    cv2.imshow("image", image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")

cv2.destroyAllWindows()
