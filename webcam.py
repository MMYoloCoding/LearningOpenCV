import cv2 as cv

capture = cv.VideoCapture(0)
cv.namedWindow('What', cv.WINDOW_FULLSCREEN)

while True:
    isTrue, frame = capture.read()
    canny = cv.Canny(frame,125,175)
    ret, thresh = cv.threshold(canny, 125, 255, cv.THRESH_BINARY)
    # cv.imshow('thresh', thresh)

    contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    print(f'{len(contours)} contour(s) found')
    
    cv.imshow('What', canny)
    if cv.waitKey(1) == ord('q'):
        break  
capture.release