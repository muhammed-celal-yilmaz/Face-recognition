import cv2
import numpy as np
#Dosyalarımız
face_cascade=cv2.CascadeClassifier(r"haarcascade_frontalface.xml")
eye_cascade=cv2.CascadeClassifier(r"haarcascade_eye.xml")

#Video üzerinde yüz ve göz tanıma
cap=cv2.VideoCapture(0)
while True:
    _, img=cap.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),4)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]

        eyes=eye_cascade.detectMultiScale(roi_gray)
        i=0
        for(ex,ey,ew,eh) in eyes:
            i+=1
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

            if(i==2):
                break

    cv2.imshow("Sample",img)

    # 'q' ile çıkış
    if cv2.waitKey(1) & 0xff==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
#Cascade trainer ile dosyalarımızı eğiterek kendi xml dosyalarımızı oluşturabiliriz.