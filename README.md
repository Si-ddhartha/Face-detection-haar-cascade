# Face-Detection
Python program that uses Haar Cascade Classifier to automatically detect faces in an image or video.

The program takes an input image or a video frame and uses OpenCV library to process it. Specifically, it applies the Haar Cascade Classifier, which is a machine learning-based approach for object detection

To use the classifier, the program first loads the pre-trained XML file that contains the features for detecting faces. It then converts the input image to grayscale and applies the classifier to detect the faces in the image. The classifier works by sliding a window over the image and comparing the features in each window to those in the XML file. If the features match, the window is considered to contain a face.

Once the program has detected the faces in the image, it draws a rectangle around each face to indicate its location. The output image with the detected faces is then displayed.

![face](https://user-images.githubusercontent.com/74449359/233853304-6159af8b-f319-4239-a398-99f08e70d6b1.png)
