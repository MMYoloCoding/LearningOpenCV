import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

# 1. Paint the image a certain color
blank[200:300, 300:400,] = 255,0,0
# cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2 ), (0,255,0), thickness=-1)
# cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (255,255,0), thickness=-1)
# cv.imshow('Circle', blank)

# 4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,255), thickness=5)
# cv.imshow('line', blank)

# 5. Write Text on image

cv.putText(blank, 'Hello, My name is MM', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0 ,(0,0,255), 2)
cv.imshow('Text', blank)
cv. waitKey(0)