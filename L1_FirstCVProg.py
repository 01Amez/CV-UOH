
import cv2
img = cv2.imread("images/lena.png")
#img = cv2.imread("images/lena.png", cv2.IMREAD_COLOR) aykat ba rangaw rang
#img = cv2.imreahttps://meet.google.com/rmf-gxey-mdfd("images/lena.png", cv2.IMREAD_GRAYSCALE)
print(img[100, 200, 1])
r = img[200:300,200:300, 2]
g = img[:,:, 1]
b = img[:,:, 0]


# b, g, r  = cv2.split(img, None)
# cv2.imshow("Red", r)
# cv2.imshow("Green", g)
# cv2.imshow("Blue", b)




img_shape = img.shape
r, c, ch = img.shape

print(r)
print(img_shape[2])

cv2.imshow("My Window", img)

cv2.waitKey()

#cv2.imwrite("images/lena_gray.jpg", img)