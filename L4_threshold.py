
import  cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("images/lena.png", 0)

ret,thresh1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
mf = cv2.medianBlur(img, 3)
cv2.imshow('img', img)
cv2.imshow('mf', mf)
cv2.imshow('threshold', thresh1)

cv2.waitKey()

