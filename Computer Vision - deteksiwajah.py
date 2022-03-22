#DETEKSI WAJAH

import cv2
import numpy as np

citra = cv2.imread('3x4.jpg')

pengklasifikasiWajah = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

abuAbu = cv2.cvtColor(citra, cv2.COLOR_BGR2GRAY)

wajah = pengklasifikasiWajah.detectMultiScale(abuAbu,
                                              scaleFactor = 1.1,
                                              minNeighbors = 1)

print('Jumlah wajah yang terdeteksi :',len(wajah))

for(x,y,w,h) in wajah:
    cv2.rectangle(citra,(x,y),(x+w,y+h),
                  (255,0,0),2)

cv2.imshow('citra ',citra)

cv2.waitKey(0)
