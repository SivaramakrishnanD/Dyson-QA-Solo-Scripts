import os, sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Select the required PNG/JPEG Files')
        self.setGeometry(10, 10, 640, 480)
        for type in ["_Master.", "_Slave."]:
            options  = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            files, _ = QFileDialog.getOpenFileNames(self, "Select " + type + " Image Files", "", "Image Files (*PNG, *JPG);;", options=options)
            if files:
                for file in files:
                    # oldname = file.split("/")
                    # oldname = oldname[-1]
                    print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
                    print("Renaming file:", file)
                    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")
                    os.rename(file, file.replace(".", type))
        sys.exit()

if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    sys.exit(app.exec_())