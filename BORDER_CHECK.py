import os, sys, cv2
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

def benjaminsmethod(IMG):
    THRESH1,THRESH2  = 75, 90
    RES           = IMG.copy()
    HEIGHT, WIDTH = IMG.shape[0], IMG.shape[1]
    RIGHTEXTREME  = RES[:,[WIDTH-1]]
    LEFTEXTREME   = RES[:,[0]]
    TOPEXTREME    = RES[[0],:]
    BOTTOMEXTREME = RES[[HEIGHT-1], :]

    RIGHTTHRESH  = (np.max(np.unique(RIGHTEXTREME, return_counts=True)[1])/np.sum(np.unique(RIGHTEXTREME, return_counts=True)[1]))*100
    LEFTTHRESH   = (np.max(np.unique(LEFTEXTREME, return_counts=True)[1])/np.sum(np.unique(LEFTEXTREME, return_counts=True)[1]))*100
    TOPTHRESH    = (np.max(np.unique(TOPEXTREME, return_counts=True)[1])/np.sum(np.unique(TOPEXTREME, return_counts=True)[1]))*100
    BOTTOMTHRESH = (np.max(np.unique(BOTTOMEXTREME, return_counts=True)[1]) / np.sum(np.unique(BOTTOMEXTREME, return_counts=True)[1])) * 100

    RIGHTRESULT  = np.all(RIGHTEXTREME  == RIGHTEXTREME[0][0])
    LEFTRESULT   = np.all(LEFTEXTREME   == LEFTEXTREME[0][0])
    TOPRESULT    = np.all(TOPEXTREME    == TOPEXTREME[0][0])
    BOTTOMRESULT = np.all(BOTTOMEXTREME == BOTTOMEXTREME[0][0])

    print("Right Corner:",  RIGHTRESULT,  RIGHTTHRESH)
    print("Left Corner:",   LEFTRESULT,   LEFTTHRESH)
    print("Top Corner:",    TOPRESULT,    TOPTHRESH)
    print("Bottom Corner:", BOTTOMRESULT, BOTTOMTHRESH)

    if RIGHTRESULT == False:
        if RIGHTTHRESH < THRESH1:
            cv2.line(RES, (WIDTH-1, 0), (WIDTH-1, HEIGHT-1), (0, 0, 255), 25)
        else:
            if RIGHTTHRESH < THRESH2:
                cv2.line(RES, (WIDTH - 1, 0), (WIDTH - 1, HEIGHT - 1), (255, 215, 0), 25)

    if LEFTRESULT == False:
        if LEFTTHRESH < THRESH1:
            cv2.line(RES, (0, 0), (0, HEIGHT-1), (0, 0, 255), 25)
        else:
            if LEFTTHRESH < THRESH2:
                cv2.line(RES, (0, 0), (0, HEIGHT - 1), (255, 215, 0), 25)

    if TOPRESULT == False:
        if TOPTHRESH < THRESH1:
            cv2.line(RES, (0, 0), (WIDTH-1, 0), (0, 0, 255), 25)
        else:
            if TOPTHRESH < THRESH2:
                cv2.line(RES, (0, 0), (WIDTH - 1, 0), (255, 215, 0), 25)

    if BOTTOMRESULT == False:
        if BOTTOMTHRESH < THRESH1:
            cv2.line(RES, (0, HEIGHT-1), (WIDTH-1, HEIGHT-1), (0, 0, 255), 25)
        else:
            if BOTTOMTHRESH < THRESH2:
                cv2.line(RES, (0, HEIGHT - 1), (WIDTH - 1, HEIGHT - 1), (255, 215, 0), 25)

    if RIGHTRESULT == False or LEFTRESULT == False or TOPRESULT == False or BOTTOMRESULT == False:
        cv2.imshow("Input", IMG)
        cv2.imshow("Result", RES)
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
                benjaminsmethod(img)
        sys.exit()

if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())





