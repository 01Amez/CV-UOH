import  cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread("images/lena.png")
my_mask = np.zeros(img1.shape[:2], np.uint8)
my_mask[200:400, 200:400] = 255
img2 = cv2.imread("images/baboon5.jpg")


res1 = cv2.add(img1, img2)
res2 = cv2.add(img1, img2, mask=my_mask)

cv2.imshow('res', res1)
cv2.imshow('mm', my_mask)
cv2.imshow('res2', res2)

res3 = cv2.add(res2, img1)
cv2.imshow('added', res3)

cv2.waitKey()



