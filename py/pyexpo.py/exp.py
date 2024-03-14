import cv2 as cv
import os 
import time 
import logging

logger = logging.getLogger()
fh = logging.FileHandler('xyz.log')
fh.setLevel(logging.DEBUG)    
logger.addHandler(fh)

cvNet = cv.dnn.readNetFromTensorflow('frozen_inference_graph.pb', 'object_detection.pbtxt')
dir_x  = "C:\\Users\\Omen\\Desktop\\LP_dataset\\anno"
for filename in os.listdir(dir_x):
    print(filename)
    if not (filename.endswith(".png") or filename.endswith(".jpg")):
        continue
    print('daz')
    img = cv.imread(os.path.join(dir_x,filename))
    img = cv.resize(img, (300,300))
    #cv.imshow('i',img)
    #cv.waitKey(0)
    img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    img = cv.cvtColor(img,cv.COLOR_GRAY2RGB)
    rows = img.shape[0]
    cols = img.shape[1]
    #cvNet.setInput(cv.dnn.blobFromImage(img, size=(cols,rows), swapRB=True, crop=False))
    cvNet.setInput(cv.dnn.blobFromImage(img, size=(300, 300), crop=False))
    t0  = time.time()
    cvOut = cvNet.forward()
    print(time.time() - t0)
    for detection in cvOut[0,0,:,:]:
        score = float(detection[2])
        #print(score)
        if score > 0.80:
            left = detection[3] * cols
            top = detection[4] * rows
            right = detection[5] * cols
            bottom = detection[6] * rows
            cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

    cv.imshow('img', img)
    cv.waitKey(0)