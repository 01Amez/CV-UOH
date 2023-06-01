import  cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("images/lena.png")

mask = np.zeros(img.shape[:2], np.uint8)
mask[220:350, 220:350] = 255

cv2.imshow('m', mask)

histb = cv2.calcHist([img],[0],mask,[256],[0,256])
histg = cv2.calcHist([img],[1],None,[256],[0,256])
histr = cv2.calcHist([img],[2],None,[256],[0,256])

plt.subplot(221), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.subplot(222), plt.plot(histr, color='r')
plt.subplot(223), plt.plot(histg, color='g')
plt.subplot(224), plt.plot(histb, color='b')



plt.show()


cv2.waitKey()

