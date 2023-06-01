
import cv2 as cv

video_capture = cv.VideoCapture(0)


if  not video_capture.isOpened() :
    print("Error: cannot open cv.VideoCapture(0).")
    exit(0)

ret1, f1 = video_capture.read()

while True:
    ret, fnew = video_capture.read()

    f1g = cv.cvtColor(f1, cv.COLOR_BGR2GRAY)

    f2g = cv.cvtColor(fnew, cv.COLOR_BGR2GRAY)

    res = cv.absdiff(f1g, f2g)

    ret, res2 = cv.threshold(res,20,255,cv.THRESH_BINARY)


    cv.imshow("Cam", res2)

    k = cv.waitKey(30)

    f1=fnew
    if k == ord('q'):
        break
