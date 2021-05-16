#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


#captures frames from a video
cap = cv2.VideoCapture('New Video.mp4')


# In[3]:


#Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')


# In[9]:


while True:
    #reads frames from a video
    ret, frames = cap.read()
    
    if (ret != True):
        break
    #convert to grayscale of each frame   
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    #detect cars of different sizes in the input
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)
    
    #draw rectangles on each car
    for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        
    #display frames in a video
    cv2.imshow('video2', frames)
    
    #wait for Esc to stop
    if cv2.waitKey(33)==27:
        break;
        
cap.release()        
#de-allocate any associated memory usage
cv2.destroyAllWindows()

