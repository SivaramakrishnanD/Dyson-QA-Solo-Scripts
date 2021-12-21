import numpy as np
import cv2, os
import matplotlib.pyplot as plt

CWD    = os.getcwd()
PATH1  = os.getcwd() + "/Inputs/DOG1.PNG"
PATH2  = os.getcwd() + "/Inputs/DOG2.PNG"
IMG1   = cv2.imread(PATH1,cv2.IMREAD_COLOR)
# IMG2   = cv2.imread(PATH2,cv2.IMREAD_COLOR)
IMG2   = cv2.resize(IMG1, (IMG1.shape[1]-100, IMG1.shape[0]-100))

SIFT   = cv2.SIFT_create()
KEYPOINTS1, DESCRIPTORS1 = SIFT.detectAndCompute(IMG1,None)
KEYPOINTS2, DESCRIPTORS2 = SIFT.detectAndCompute(IMG2,None)
BF      = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
MATCHES = BF.match(DESCRIPTORS1,DESCRIPTORS2)
MATCHES = sorted(MATCHES, key = lambda x:x.distance)

for match in MATCHES[:15]:
    RES = cv2.drawMatches(IMG1, KEYPOINTS1, IMG2, KEYPOINTS2, [match], IMG2, flags=2)
    plt.imshow(RES),plt.show()

# cv2.imshow("Input", IMG1)
# cv2.imshow("Result",RES)
# cv2.waitKey(0)
# cv2.destroyAllWindows()