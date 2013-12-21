import numpy as np
import cv2
def convertMTStoJPG(source,target):
    cap = cv2.VideoCapture(source)
    i=0
    while(cap.isOpened()):
        ret, frame = cap.read()
    
        i=i+1 
        cv2.imwrite(target+str(i)+'.jpg',frame)
        print(target+str(i)+'.jpg')
        if frame is None:
            break
        
        

    cap.release()
cv2.destroyAllWindows()
