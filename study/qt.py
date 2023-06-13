from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
from os import path
import sys



formclass,_= loadUiType(path.join(path.dirname(__file__),'D:\\python\\untitled.ui'))


class liondownloader(QMainWindow, formclass):
    def __init__(self,parent=None):
        super(liondownloader,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)



def main():
    app = QApplication(sys.argv)
    window = liondownloader()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()