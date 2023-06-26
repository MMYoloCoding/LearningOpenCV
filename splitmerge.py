import cv2 as cv 
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('cats' , img)

b,g,r = cv.split(img)
blank = np.zeros (img. shape [:2], dtype= 'uint8')

blue = cv.merge([b,blank,blank])
green = cv.merge ([blank, g, blank])
red = cv. merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

print(img.shape) #x,y,color channel
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r]) #merging the three color channel back
cv.imshow('merge', merged)
cv.waitKey (0)