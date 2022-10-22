import cv2
import argparse

def detecAndDisplay(frame):
    frame_gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray=cv2.equalizeHist(frame_gray)

    cat_face=face_cascade.detecctMultiScale(frame_gray)

#haarcascade

#누리 평균값 색

#향이 평균값 색

#동생이 평균값 색



for image in ('C:/Users/cat7892/Documents/GitHub/catholic/cat_detection/test'):
