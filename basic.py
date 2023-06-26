import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('lady', img)

# Convering to grayscale (intensity distribution of pixels) 
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Cat', gray)

# Blur 
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
# cv.imshow("Canny", canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (7,7) , iterations=3)
# cv.imshow('Eroded', eroded)

# Resize (INTER_AREA for shrinking, INTER_LINE for enlarging)
resized = cv.resize(img, (5000,3000), interpolation=cv.INTER_CUBIC)
# cv.imshow('resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)
cv.waitKey(0)