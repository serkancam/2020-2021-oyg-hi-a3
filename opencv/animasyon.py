import cv2
import numpy as np
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QImage, QPixmap
import time

class Uygulama(QMainWindow):
    def __init__(self):
        super(Uygulama,self).__init__()
        self.cd = os.getcwd()
        self.ui_path=os.path.join(self.cd,"opencv","animasyon.ui")
        self.InitUI()

    def InitUI(self):
        self.win = uic.loadUi(self.ui_path,self)
        # butonların tıklanıldığını algılıyorum
        self.win.btnOynat.clicked.connect(self.oynat)
        self.win.btnDurdur.clicked.connect(self.durdur)
        self.win.show()
    def oynat(self):#btnOynat butonuna tıklandığında aşağıdaki işlemler yapılacak
        resim_yolu = os.path.join(self.cd,"opencv","images","chp2","zebrasmall.png")
        resim = cv2.imread(resim_yolu)
        h,w,c = resim.shape
        g_resim = QImage(resim.data,w,h,c*w,QImage.Format_RGB888)
        self.win.lblGoruntu.setPixmap(QPixmap.fromImage(g_resim))
        
    def durdur(self):
        pass

if __name__ == "__main__":
    uyg = QApplication(sys.argv)
    uygulama = Uygulama()
    sys.exit(uyg.exec_())
