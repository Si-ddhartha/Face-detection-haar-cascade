import cv2 as cv

# Using the main camera(0) for taking the video input
cap = cv.VideoCapture(0)

haar_cascade = cv.CascadeClassifier('haar_cascade_face.xml')

while True:
    # Reading the frame
    isTrue, frame = cap.read()

    if isTrue:
        # Converting the frame to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Detecting the faces in the frame
        faces = haar_cascade.detectMultiScale(gray, 1.1, 3)

        # Drawing rectangle over every face detected
        for x, y, w, h in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv.imshow("Video", frame)

        if cv.waitKey(20) & 0xFF == ord('d'):  # Video will close iff 'd' key is pressed
            break

    else:
        break

cap.release()
cv.destroyAllWindows()
