# Human-and-Vehicle-Detection-OpenCV
The objective of the program given is to detect object of interest(Car, Humans) in video frames and to keep tracking the same object. This is an example of how to detect vehicles in OpenCV and Python.

## What is OpenCV?
OpenCV is an open-source library, which is aimed at real-time computer vision. This library is developed by Intel and is cross-platform – it can support Python, C++, Java, etc. Computer Vision is a cutting edge field of Computer Science that aims to enable computers to understand what is being seen in an image. OpenCV is one of the most widely used libraries for Computer Vision tasks like face recognition, motion detection, object detection, etc.

## Why is it useful?
Pedestrian and vehicle detection is a very important area of research because it can enhance the functionality of a pedestrian protection system and can prevent the losses both in human life and finance caused by vehicle accidents.

### For pedestrian detection -
We can extract features like head, two arms, two legs, etc, from an image of a human body and pass them to train a machine learning model. After training, the model can be used to detect and track humans in video streams. However, OpenCV has a built-in method to detect pedestrians. It has a pre-trained HOG(Histogram of Oriented Gradients) + Linear SVM model to detect pedestrians in video streams.

### For Vehicle detection
OpenCV has a built-in method to detect objects like vehicles. It has a pre-trained Cascade-Classifier.

### Libraries Used - 
OpenCV
imutils
