import cv2
import numpy as np 
import face_recognition

imgElon = face_recognition.load_image_file('ImagesBasic\Elon Test.jpeg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic\Elon Musk.jpeg')
imgTest = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

cv2.imshow('Elon Musk',imgElon)
cv2.imshow('Elon Test',imgTest)
cv2.waitKey(0)