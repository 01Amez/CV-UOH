import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


src = cv.imread('images/tomato.png')

src_hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

cv.imshow('src', src)
cv.imshow('hsv', src_hsv)


dst = cv.inRange(src_hsv, (0, 100, 20), (10, 255, 255))
cv.imshow('dst', dst)

cv.waitKey()
