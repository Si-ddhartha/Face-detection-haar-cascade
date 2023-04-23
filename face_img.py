import cv2 as cv
from image0 import resize

# Reading the input image
img = cv.imread(file_path)

# Resizing the image (if image is large)
img_resized = resize(img, 0.25)

# Converting the image to grayscale
gray = cv.cvtColor(img_resized, cv.COLOR_BGR2GRAY)

# Face Detection
haar_cascade = cv.CascadeClassifier('haar_cascade_face.xml')
faces = haar_cascade.detectMultiScale(gray, 1.1, 3)

# Drawing rectangle over all detected faces
for x, y, w, h in faces:
    cv.rectangle(img_resized, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('Faces', img_resized)

cv.waitKey(0)
