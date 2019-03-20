'''
Created on Mar 13, 2019

@author: ajacobs
'''
import sys
from PySide2 import QtWidgets

from dnd.ui_pyside.main import UI

from dnd.engine.player import Player

class LaunchUI(UI):
    def __init__(self):
        super(LaunchUI, self).__init__(Player)

if __name__=='__main__':
    print ('launch')
    app = QtWidgets.QApplication(sys.argv)
    qtApp = LaunchUI()
    qtApp.show()
    app.exec_()
   
'''
from dnd.UI.designer.testWidget import Ui_MainWindow
  
class LaunchUI(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(LaunchUI, self).__init__()
        self.setupUi(self)
if __name__=='__main__':
    print ('launch')
    app = QtWidgets.QApplication(sys.argv)
    qtApp = LaunchUI()
    qtApp.show()
    app.exec_()
'''