import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
import numpy as np
import cv2

def houghlineapproach(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    newimg = img.copy()
    edges = cv2.Canny(gray, 50, 150)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
    for index, line in enumerate(lines):
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        thetarange1 = (np.pi / 2) * 0.8
        thetarange2 = (np.pi / 2) * 1.2
        # print(print("Line", theta, (x1, y1), (x2, y2)))
        # FINDING VERTICAL LINES
        if theta == 0.0:
            if x1 == x2:
                print("Vertical Line", theta, (x1, y1), (x2, y2))
                cv2.line(newimg, (x1, y1), (x2, y2), (0, 255, 255), 6)

        # FINDING HORIZONTAL LINES
        if theta > thetarange1 and theta < thetarange2:
            if y1 == y2:
                print("Horizontal Line", theta, (x1, y1), (x2, y2))
                cv2.line(newimg, (x1, y1), (x2, y2), (0, 255, 255), 6)

    cv2.imshow("Input", img)
    cv2.imshow("Result", newimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Select the required PNG/JPEG Files')
        self.setGeometry(10, 10, 640, 480)

        options  = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Select Image Files", "", "Image Files (*PNG, *JPG);;", options=options)
        if files:
            for file in files:
                img = cv2.imread(file, cv2.IMREAD_COLOR)
                print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                print("Reading file:", file, "Size:", img.shape)
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                houghlineapproach(img)
        sys.exit()

if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())
