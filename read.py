import cv2 as cv

# Reading Image (OpenCV reads in image as a format of BGR)

# img = cv.imread('Photos/cat_large.jpg')

# cv.imshow('Cat', img)

# Reading Video

capture = cv.VideoCapture('Videos/dog.mp4')


while True:
    isTrue, frame = capture.read()
    # frame_text = cv.putText(frame, "Hello I am a cute puppy", (255,255),cv.FONT_HERSHEY_TRIPLEX, 1.0 ,(0,0,255), 2)
    # frame = cv.Canny(frame, 125,175)
    # filtered_frame = cv.blur(frame, (111,111))
    cropped = frame[0:5000, 500:5000]
    cv.imshow('Video', cropped)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
