# Automatic-predict-whether-a-person-wear-mask-or-not.

## Description
Real-time Face Without Mask recognition project with OpenCV and Python

* Recognising Face Without Mask
```
import cv2

face_recognize = cv2.CascadeClassifier('haarcascade_face_without_mask.xml')                                 # Assigning XML file

cap = cv2.VideoCapture(0)                                                                                   # Capture Video 

while 1: 
    ret, img = cap.read()                                                                                   # Reading Live Video
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    face_without_mask_recognized = face_recognize.detectMultiScale(gray, 1.3, 5)                            # Detecting FaceWithoutMask

    for (x,y,w,h) in face_without_mask_recognized:
        face_without_mask = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)                                  # Marking out a rectangle on Face
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'Person_Without_Wearing_Mask',(x-w,y-h), font, 0.5, (11,255,255), 2, cv2.LINE_AA)   # Put text on Face Rectangle 
```

![Image](https://banner2.cleanpng.com/20180629/bxv/kisspng-stock-photography-bigstock-portrait-indian-men-5b35fe828482e9.4087547415302652185428.jpg) 

* Image showing
```
    cv2.imshow('img',img)   
    k = cv2.waitKey(30) & 0xff   
    if k == 27:                 
        break
```

* Destroy all windows
```
cap.release()
cv2.destroyAllWindows()   
```

## Table of Contents
* [Description](#Description)
* [Installation](#Installation)

# Installation

## Requirements
* Python 3.3+
* macOS or Linux (Windows not officially supported, but might work)

## Installation Options:

### Installing on Mac or Linux
First, make sure you have installed Python 3.3+ on your machine.
* [Install Python](https://realpython.com/installing-python/)
* Install OpenCV package on terminal

```
 pip install opencv-python

           or

 sudo apt install python3-opencv
```