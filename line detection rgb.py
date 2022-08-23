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
status , photo = cap.read()
status

while True:
    status, photo = cap.read()

    
    converted = grey(photo)
    converted1 = cv2.GaussianBlur(converted, (5, 5 ), 0)
    converted2 = cv2.Canny(converted1,20, 70)

    lines = cv2.HoughLinesP(converted2, 1, np.pi/180, 10, minLineLength =50, maxLineGap =10)
    b = 0
    g = 0
    r = 0
    for line in lines:
        x1,y1, x2, y2 = line[0]
        cv2.line(photo,(x1, y1), (x2, y2), (b,g ,r ) , 2)
        b += 40
        g += 70
        r += 100
        if b > 255:
            b = 0
        if g > 255:
            g = 0
        if r > 255:
            r = 0
        
    cv2.imshow('MY PIC',photo)
    if cv2.waitKey(100) == 27:
        break

cv2.destroyAllWindows()
cap.release()