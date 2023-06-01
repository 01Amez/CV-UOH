import cv2 as cv

video_capture = cv.VideoCapture(0)

fps = video_capture.get(5)




# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
output = cv.VideoWriter('E:\\amez\\UOH\\stage3\s2\\vision\\cam\\outpy2.avi', cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (640, 480))

print(["FPS: ", cv.CAP_PROP_FPS ,fps])
if not video_capture.isOpened():
    print("Error: cannot open cv.VideoCapture(0).")
    exit(0)


while True:
    ret, frame = video_capture.read()

    if frame is None:
        print("Empty Frame Was Read!")

    cv.imshow("Cam", frame)
    output.write(frame)
    k = cv.waitKey(30)

    if k == ord('q'):
        break



cv.destroyAllWindows()
output.release()
video_capture.release()
