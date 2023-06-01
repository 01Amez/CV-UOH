import cv2
import numpy
img = cv2.imread("images/lena.png")
img = cv2.imread("images/lena.png", cv2.IMREAD_COLOR)
# img = cv2.imread("images/lena.png", cv2.IMREAD_GRAYSCALE)

# print(type(img))


res = img.shape
r, c, ch = img.shape #row colom chanel

print(res[2])
print(ch)


# accesing pixel value
px = img[200, 150, 2]
print(px)


roi = img[:,100:400]

b = img[:, :, 0]
g = img[:, :, 1]
r = img[:, :, 2]

bc, gc, rc = cv2.split(img, None)


r[100:200, :] = 0

# r[240, 1] = 97
# r[240, 2] = 108
# r[240, 3] = 105

merged_img = cv2.merge((b,g,r), None)

cv2.imshow("My Window", img)
cv2.imshow("Merged", merged_img)


cv2.waitKey()

# cv2.imwrite("lena_g.jpg", img)

