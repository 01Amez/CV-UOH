import  cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread("images/lena.png")

img2 = cv2.imread("images/baboon5.jpg")


res = cv2.add(img1, img2)


cv2.imshow('res', res)

cv2.waitKey()



