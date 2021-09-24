import argparse
import os
import cv2
from wand.image import Image
import numpy as np

#ArgumentParser객체:명령행을 파이썬 데이터형으로 파싱하는데 필요한 모든 정보가 들어있음
#ArgumentParser객체 생성
ap=argparse.ArgumentParser()
ap.add_argument("-i","--images",required=True, help="absolute path to the input image")
ap.add_argument("-c","--cascade",default="C:/Users/cat7892/Documents/GitHub/catholic/catface_detection/haarcascade_frontalcatface.xml",help="absolute path to detector haar cascade")
#parse_args():문자열을 객체로 변환 후 namespace의 attribute로 설정
args=vars(ap.parse_args())
count=0

#imagefolder->only heic, jpg type images
imagefolder=args['images'].replace('\\','/')
for image in os.listdir(args["images"]):
    print(image)
    #If the image file format is 'heic', it is converted to 'jpg'.
    if image[-3:]!='jpg':
        img=Image(filename=imagefolder+'/'+image)
        img.format='jpg'
        image=image.replace('heic', 'jpg')
        img.save(filename=imagefolder+'/'+image)
        img.close()
        os.remove(imagefolder+'/'+image.replace('jpg','heic'))
'''
    # load image+convert grayscale
    color=cv2.imread(imagefolder+'/'+image)
    gray=cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
    #load detector, then detect
    detector=cv2.CascadeClassifier(args["cascade"])
    rects=detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10)

    #loop over detect and save file
    for (i, (x,y,w,h)) in enumerate(rects):
        roi=color[y:y+h,x:x+w].copy()
        print(x,y,w,h)
        cv2.imwrite('C:/Users/cat7892/Documents/GitHub/catholic/catface_detection/test_detect/'+str(count)+'.jpg',roi)
        cv2.waitKey()
        count+=1
'''