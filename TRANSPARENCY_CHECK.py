import os, sys, cv2, io, re
import numpy as np
import matplotlib.pyplot as plt
from google.cloud import vision
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from skimage.metrics import structural_similarity

def mse(master, slave):
    err = np.sum((master.astype("float") - slave.astype("float")) ** 2)
    err /= float(master.shape[0] * slave.shape[1])
    return err

def transparency_check(MASTERPATH, SLAVEPATH):
    IMAGES = []
    for IMGPATH in [MASTERPATH, SLAVEPATH]:
        IMG       = cv2.imread(IMGPATH, cv2.IMREAD_COLOR)
        boxthresh = 8
        ssthresh  = 0.95
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/sivaramakrishnand/Desktop/TESTS/GOOGLE VISION TEST/cred.json"

        with io.open(IMGPATH, 'rb') as imagefile:
            imagedata = imagefile.read()

        client   = vision.ImageAnnotatorClient()
        image    = vision.Image(content=imagedata)
        response = client.text_detection(image=image)
        texts    = response.text_annotations
        for index, item in enumerate(texts):
            if index != 0:
                coordinates = []
                for index, vertex in enumerate(item.bounding_poly.vertices):
                    coordinates.append((vertex.x, vertex.y))
                coordinates[0] = (coordinates[0][0] - boxthresh, coordinates[0][1] - boxthresh)
                coordinates[2] = (coordinates[2][0] + boxthresh, coordinates[2][1] + boxthresh)
                cv2.rectangle(IMG, coordinates[0], coordinates[2], (0, 0, 0), -1)
        IMAGES.append(IMG)

    MSE  = mse(IMAGES[0], IMAGES[1])
    SSIM = structural_similarity(IMAGES[0], IMAGES[1], multichannel=True)

    if SSIM < ssthresh:
        print("Structural Similarity: {ssm:.2f} %".format(ssm=SSIM * 100))
        fig = plt.figure(MASTERPATH, [10, 8])
        plt.suptitle("Structural Similarity: {ssm:.2f} %".format(ssm=SSIM * 100))
        ax = fig.add_subplot(1, 2, 1)
        plt.imshow(IMAGES[0], cmap=plt.cm.gray)
        plt.axis("off")
        ax = fig.add_subplot(1, 2, 2)
        plt.imshow(IMAGES[1], cmap=plt.cm.gray)
        plt.axis("off")
        plt.show()
    else:
        print("No Transparency issues found")
        print("Structural Similarity: {ssm:.2f} %".format(ssm=SSIM * 100))

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Select the required PNG/JPEG Files')
        self.setGeometry(10, 10, 640, 480)

        # options  = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # files, _ = QFileDialog.getOpenFileNames(self, "Select Image Files", "", "Image Files (*PNG, *JPG);;", options=options)
        # if files:
        #     mfiles = []
        #     sfiles = []
        #     for filepath in files:
        #         if re.search("master", filepath):
        #             mfiles.append(filepath)
        #         else:sfiles.append(filepath)
        #
        #     files = []
        #     for mfile in mfiles:
        #         file1 = mfile.replace("master", "")
        #         for sfile in sfiles:
        #             file2 = sfile.replace("slave", "")
        #             if file1 == file2:
        #                 files.append([mfile, sfile])
        #
        #     for filepaths in files:
        #         if len(filepaths) == 2:
        #             print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        #             print("Reading Master File:", filepaths[0], "\nReading Slave File:", filepaths[1])
        #             print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
        #             transparency_check(filepaths[0], filepaths[1])

        mfiles = []
        sfiles = []
        for type in ["Master", "Slave"]:
            options  = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            files, _ = QFileDialog.getOpenFileNames(self, "Select " + type + " Files", "", "Image Files (*PNG, *JPG);;", options=options)
            if type == "Master":
                mfiles = files
            else:
                sfiles = files

        files = []
        for mfile in mfiles:
            file1 = mfile.split("/")[-1]
            for sfile in sfiles:
                file2 = sfile.split("/")[-1]
                if file1 == file2:
                    files.append([mfile, sfile])

        for filepaths in files:
            if len(filepaths) == 2:
                print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                print("Reading Master File:", filepaths[0], "\nReading Slave File:", filepaths[1])
                print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                transparency_check(filepaths[0], filepaths[1])
        sys.exit()

if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())