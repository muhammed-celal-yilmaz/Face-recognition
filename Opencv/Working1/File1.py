import cv2
import numpy as np

print("OpenCV sürümü:",cv2.__version__)
resim=cv2.imread("kv.jpg",0)
#np array tipinde resim
#0 parametresiyle rengi gri yaptık
print(type(resim))
cv2.imshow("KV",resim)#resim gösterme
#resminden bağımsız bu gri resmi kaydet:
cv2.imwrite("kv_gri.jpg",resim)


cv2.waitKey(0)
cv2.destroyAllWindows()
