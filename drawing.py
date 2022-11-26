import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)

print(img.shape)

# adding color to an image
# img[:] = 255, 0, 0

# drawing a line
cv.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

cv.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)

cv.circle(img, (400, 50), 30, (255, 255, 0), 5)

cv.putText(img, 'Franklin', (300, 200),
           cv.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)


cv.imshow('Image', img)

cv.waitKey(0)


# Another one

blank = np.zeros((500, 500), dtype='uint8')
cv.imshow('Blank', blank)

# Paint the image in a certain color
blank[200:300, 300:400] = 0, 0, 255
cv.imshow("GREEN", blank)

# Draw rectangle
cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=-1)
cv.imshow("Reactangle", blank)
