"""
So far, basic face detection; draws red box around each face
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(-1)
#change the string to the location of this file on your computer
face_cascade = cv2.CascadeClassifier('/home/rebecca/Documents/Hackathon/Codestellation15/haarcascade_frontalface_alt.xml')

while True:
    ret, frame = cap.read() # captures each frame
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize = (20,20))
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y), (x+w, y+h), (0,0,255))

    cv2.imshow('frame', frame) #shows the frame
    if cv2.waitKey(1) & 0xFF == ord('q'): #press q to close
        break

cap.release()
cv2. destroyAllWindows
