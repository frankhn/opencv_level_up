import cv2 as cv

capture = cv.VideoCapture("Videos/dog.mp4")

# Changing the resolution of the image
def changeRes(width, height):
    # Live vide
    capture.set(3, width)
    capture.set(4, height)

def rescaleFrame(frame, scale=.6):
    # Works for Live Video and images
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video Captured', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
