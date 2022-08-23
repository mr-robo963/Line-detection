import numpy as np
import cv2
import matplotlib.pyplot as plt


def grey(image):
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
def gauss(image):
    return cv2.GaussianBlur(image, (5, 5 ), 0)
def canny(image):
    edges = cv2.Canny(image,50,130)
    return edges


cap = cv2.VideoCapture(0)  
# cap = cv2.VideoCapture('https://10.41.0.104:8080/video')  
status , photo = cap.read()

while True:
    status, photo = cap.read()
    
    converted = grey(photo)
    converted1 = gauss(converted)
    converted2 = canny(converted1)

    lines = cv2.HoughLinesP(converted2, 1, np.pi/180, 10, minLineLength =50, maxLineGap =10)
    for line in lines:
        x1,y1, x2, y2 = line[0]
        cv2.line(photo,(x1, y1), (x2, y2), (0, 250, 0) , 1)
    
    cv2.imshow('MY PIC',photo)

    if cv2.waitKey(100) == 27:
        break

cv2.destroyAllWindows()
cap.release()