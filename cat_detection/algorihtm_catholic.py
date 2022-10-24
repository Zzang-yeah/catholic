import cv2
import argparse

# USAGE
# python cat_detector.py --image images/cat_01.jpg

# import the necessary packages
import argparse
import cv2

import os

os.system('mode con: cols=100 lines=40')
input("Press any key to continue...")

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                default="C:/Users/cat7892/Documents/GitHub/catholic/cat_detection/mycats/",
                help="path to the input image")
ap.add_argument("-c", "--cascade",
                default="C:/Users/cat7892/Documents/GitHub/catholic/CatDetection-HaarCascade/haarcascade_frontalcatface.xml",
                help="path to cat detector haar cascade")
args = vars(ap.parse_args())

# load the input image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the cat detector Haar cascade, then detect cat faces in the input image
detector = cv2.CascadeClassifier(args["cascade"])
rects = detector.detectMultiScale(gray, scaleFactor=1.3,
                                  minNeighbors=10, minSize=(75, 75))

# loop over the cat faces and draw a rectangle surrounding each
for (i, (x, y, w, h)) in enumerate(rects):
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
# write the image
cv2.imwrite('result.jpg', image)
image=cv2.resize(image, dsize=(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
# show the detected cat faces
cv2.imshow("Cat Faces", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#haarcascade

#누리 평균값 색

#향이 평균값 색

#동생이 평균값 색



#for image in ('C:/Users/cat7892/Documents/GitHub/catholic/cat_detection/test'):