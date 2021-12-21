import cv2
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def cannyapproach(img):
    edges = cv.Canny(img,100,100)

    separationcount = 0
    masterseparator = None
    separatorlist   = []

    for separator, pixel in enumerate(reversed(edges[1])):
        print('Column No:', edges.shape[1] - separator - 1)
        print(edges[1:, [edges.shape[1] - separator - 1]].transpose())
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        if pixel != 0:
            # print(separator, edges[1:, [edges.shape[1] - separator - 1]])
            if np.all(edges[1:, [edges.shape[1] - separator - 1]] == 255):
                masterseparator = edges.shape[1] - separator - 1
                separatorlist.append(masterseparator)
                separationcount = + 1
                print("Separation identified at column number:", masterseparator, "Iteration no:", separator)
                if np.all(edges[1:, [edges.shape[1] - separator - 2]] == 255):
                    break

    if separationcount == 0:
        print("No borders found")
    elif separationcount == 1:
        print("1PX border found at the column number:", masterseparator)
        plt.subplot(131), plt.imshow(img, cmap='gray')
        plt.title('Original Image' + str(img.shape)), plt.xticks([]), plt.yticks([])
        plt.subplot(132), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(133), plt.imshow(edges, cmap='gray')
        plt.plot([masterseparator, masterseparator], [0, edges.shape[0]], color="red", linewidth=3)
        plt.title('Canny edge detection'), plt.xticks([]), plt.yticks([])
        plt.show()
    else:
        print("Several vertical lines or multipixel borders found at columns:", separatorlist)

    if separationcount != 1:
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image' + str(img.shape)), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

img = cv.imread('Dyson_FC_674_Group_EN_Digital_A1_Static_160x600_SEE.jpg', cv.IMREAD_COLOR)
cannyapproach(img)