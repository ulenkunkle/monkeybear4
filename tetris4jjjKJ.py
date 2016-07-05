
import cv2 
import numpy as np


face_cascade = cv2.CascadeClassifier('C:\\tmp\\haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('C:\\tmp\\haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

#fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
#out = cv2.VideoWriter('C:\\tmp\\output8ab.mp4',fourcc, 20.0, (640,480))
out = cv2.VideoWriter('C:\\tmp\\output7babaa.avi',-1, 20.0, (640,480),1)
while True:

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (225,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'ISIS -->',(x-w,y-h+120), font, 0.5, (11,255,255), 2, cv2.LINE_AA)
        eyes = eye_cascade.detectMultiScale(roi_gray)


        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew,ey+eh), (0,255,0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,'   <----ISIS',(x+w,y+h-80), font, 0.5, (2,2,255), 2, cv2.LINE_AA)
    out.write(img)
    cv2.imshow('img',img)


    if cv2.waitKey(1) & 0xFF == ord('q'):

       break

    # if k == 27:


        # break



cap.release()
out.release()
cv2.destroyAllWindows()
 


# 30.Traceback (most recent call last):


# 31.  File "C:Python27briansdetector.py", line 13, in <module>


# 32.    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


# 33.error: C:buildsmaster_PackSlaveAddon-win32-vc12-staticopencvmodulesobjdetectsrccascadedetect.cpp:1639: error: (-215) !empty() in function cv::CascadeClassifier::detectMultiScale
