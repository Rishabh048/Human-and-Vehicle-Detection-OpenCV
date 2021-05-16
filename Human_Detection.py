#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import the libraries
import cv2
import imutils


# In[3]:


# initializing the HOGDescriptor for person detection
HOGCV = cv2.HOGDescriptor()
HOGCV.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

#get the video file by specified path
video = cv2.VideoCapture('run.mp4')


# In[4]:


# open the video and check its running
while video.isOpened():
    check, frame = video.read()
    if check:
        # resize the output of video file
        frame = imutils.resize(frame, width=min(800, frame.shape[1]))
        bounding_box_cordinates, weights = HOGCV.detectMultiScale(frame, winStride=(4, 4), padding=(8, 8),
                                                              scale=1.03)
        # create person var for count of people
        person = 0
        # define the dimensions and text of rectangular boxes identifying humans
        for x, y, w, h in bounding_box_cordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'person {person}', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            person += 1
            cv2.putText(frame, 'Status : Detecting', (40, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                                                        (255, 255, 0), 1)
            cv2.putText(frame, f'Total People : {person}', (40, 70), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (255, 255, 0), 1)
            # get the output video
            cv2.imshow('output', frame)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
    else:
        break
video.release()
cv2.destroyAllWindows()

