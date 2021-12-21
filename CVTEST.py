import cv2
import os
import numpy as np

# ARR = np.array([[[[555,555]]], [[[555,45]]], [[[555,555]]]])
# # RES = np.all(ARR == ARR[0][0])

CWD  = os.getcwd()
PATH = os.getcwd() + "/Inputs/Dyson_FC_674_Group_EN_Digital_A1_Static_160x600_SEE.jpg"
IMG  = cv2.imread(PATH, cv2.IMREAD_COLOR)
SIFT = cv2.SIFT_create()
KEYPOINTS1, DESCRIPTORS1 = SIFT.detectAndCompute(IMG,None)

RES  = cv2.drawKeypoints(IMG, KEYPOINTS1, IMG)
cv2.imshow("IMAGE", IMG)
cv2.imshow("RESULT",RES)
cv2.waitKey(0)
cv2.destroyAllWindows()





