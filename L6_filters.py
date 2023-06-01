import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


src = cv.imread('images/R.jpg')

#Average
#dst = cv.blur(src, (9,9))

#Gauusian
dst = cv.GaussianBlur(src, (9,9), 0)


kernel = np.ones((3,3), np.float32)/9
print(kernel)

kernel2 = np.array([
    [1,0,-1],
    [1,0,-1],
    [1,0,-1]
    ])
#custome filter
#dst = cv.filter2D(src, -1, kernel2)

dst = cv.Canny(dst, 150, 200)
cv.imshow('src', src)
cv.imshow('dst', dst)


cv.waitKey()


