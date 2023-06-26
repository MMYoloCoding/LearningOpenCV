import cv2 as cv
import matplotlib.pyplot as plt #display RGB image, can see coordinate of each pixel, but will convert color 
img = cv. imread ('Photos/cats.jpg')
cv.imshow ('cats', img)

# plt.imshow(img)
# plt.show()
# BGR to Grayscale
gray = cv.cvtColor (img, cv .COLOR_BGR2GRAY)
cv.imshow ('Gray', gray)


#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# BGR to LAB L=a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb) #this will still convert the color

plt.imshow(rgb) #This is the original image
# plt.show()

#HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR', hsv_bgr)

#gray to hsv
gray_bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('NEW1', gray_bgr)
bgr_hsv = cv.cvtColor(gray_bgr, cv.COLOR_BGR2HSV)
cv.imshow('NEW2', bgr_hsv)


cv.waitKey(0)