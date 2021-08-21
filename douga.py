import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
 
#保存
fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
fps = 20.0
size = (640, 360)
writer = cv2.VideoWriter('outtest.m4v', fmt, fps, size)

k=0
while True:
    k = k+1
    _, frame = cap.read()
    frame = cv2.resize(frame, size)
     
    #保存
    writer.write(frame)
     
    cv2.imshow('frame', frame)
    #Enterキーで終了
    #if cv2.waitKey(1) == 13:
    if k == 150:
        break
 
#保存
writer.release()
cap.release()
cv2.destroyAllWindows()
print("Hello World")
