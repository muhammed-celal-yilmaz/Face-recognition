import cv2
import numpy

#Sadece resim üzerinde yüz tanıma
face_cascade=cv2.CascadeClassifier(r"haarcascade_frontalface.xml")
img=cv2.imread(r"M.Ali.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
faces=face_cascade.detectMultiScale(gray,1.2,5)

for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)

cv2.imshow('Image',img)
cv2.waitKey(0)
