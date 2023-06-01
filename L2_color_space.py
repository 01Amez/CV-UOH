import cv2

import numpy as np

from matplotlib import pyplot as plt


def is_color(img):

    sh = img.shape

    if len(sh) >=3 :
        return True
    else:
        return False

img = cv2.imread("images/lena.png")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


cv2.imshow("hsv", hsv_img)
plt.subplot(2,2,1),plt.imshow(rgb_img),plt.title('Original')
plt.subplot(2,2,2),plt.imshow(img),plt.title('RGB')
plt.subplot(2,2,3),plt.imshow(gray_img, cmap='gray'),plt.title('Gray') # atwani cmap esh nanwsen
plt.subplot(2,2,4),plt.imshow(hsv_img, cmap=None),plt.title('HSV') #atwani ba r g b pey bae balam dabe cmap bkay ba gray chwnka bas hsaby aw rangay daka
plt.show()

cv2.waitKey()

