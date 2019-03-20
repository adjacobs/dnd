'''
Created on Mar 13, 2019

@author: ajacobs
'''
import sys
from PySide2 import QtWidgets

from dnd.UI import dndUI

class MainUI(dndUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    qtApp = MainUI()
    qtApp.show()
    app.exec_()
