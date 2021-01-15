import cv2
import numpy as np

img = cv2.imread('./assets/3.jpg')

kernel = np.ones((5,5), np.uint8)

cv2.imshow('any name', img)
# Learning about image conversions
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)

imgCanny = cv2.Canny(img,  150, 200)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)

imgEroded = cv2.erode(imgDilation, kernel, iterations=1)

cv2.imshow('gray image', imgGray)
cv2.imshow('Blur image ', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilation Image', imgDilation)
cv2.imshow('Eroded Image', imgEroded)

# Resizing the image
print(img.shape)

imgResized = cv2.resize(img, (300, 200))

cv2.imshow('Resized image', imgResized)

# check the resized image shape
print(imgResized.shape)


# Cropping images
imgCropped = img[0:200, 200:500]
cv2.imshow('Cropped image', imgCropped)

cv2.waitKey(0)