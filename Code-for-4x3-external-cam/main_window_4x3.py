import time
# import system module
import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

# import Opencv module
import cv2

from ui_main_window import *
#import
from detect import detect
class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)
        self.ui.pushButton.clicked.connect(self.count)

    # view camera
    def count(self):
        ret,frame=self.cap.read()
        count,img = detect(frame)
        self.ui.numlabel.setText(count.__str__())
        #show result
        # convert image to RGB format
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = img.shape
        step = channel * width
        # create QImage from image
        qimage = QImage(img.data, width, height, step, QImage.Format_RGB888)
        # show image in image_label
        self.ui.image_label_2.setPixmap(QPixmap.fromImage(qimage))
    def viewCam(self):
        # read image in BGR format
        ret, image = self.cap.read()
        # convert image to RGB format
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # get image infos
        height, width, channel = image.shape
        step = channel * width
        # create QImage from image
        qimage = QImage(image.data, width, height, step, QImage.Format_RGB888)
        # show image in image_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qimage))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap = cv2.VideoCapture(1)
            self.cap.set(3, 640)
            self.cap.set(4, 480)
            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap.release()
            # update control_bt text
            self.ui.control_bt.setText("Start")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
