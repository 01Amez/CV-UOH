import cv2 as cv

video_capture = cv.VideoCapture(0)


if  not video_capture.isOpened() :
    print("Error: cannot open cv.VideoCapture(0).")
    exit(0)

i = 0
while True:
    ret, frame = video_capture.read()

    if frame is None:
        print("Empty Frame Was Read!")
        break




    ig = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("Cam", frame)
    cv.imshow("gray", ig)
    #i = i + 1
   # cv.imwrite("E:\\amez\\UOH\\stage3\\s2\\vision\\cam" + str(i) + ".jpg", frame)


    k = cv.waitKey(30)

    if k == ord('q'):
        break
    if k == ord('s'):
        i = i +1
        cv.imwrite("E:\\amez\\UOH\\stage3\s2\\vision\\cam\\screen"+str(i)+".jpg", frame)

