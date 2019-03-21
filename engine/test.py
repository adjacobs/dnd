

from PySide2 import QtCore, QtGui, QtWidgets
import sys

class TestWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super(TestWidget, self).__init__()
        print('Cat')
        
        self.setObjectName("MainWindow")
        self.resize(836, 1051)

        #Set up central widget for the main window that allows other widgets to be added to.
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        
        #Sets up central widget layout for central widget that all UI elements will be added to
        self.centralGLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.centralGLayout.setObjectName("centralGLayout")
        
        #Setting paramaters for QFrame inherited class
        self.frame = QtWidgets.QFrame()
        self.frame.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.layout = QtWidgets.QVBoxLayout(self.frame)
        
        self.centralGLayout.addWidget(self.frame)
        
        #Setting layout that frame uses
        button1 = QtWidgets.QPushButton()
        button2 = QtWidgets.QPushButton()
        button3 = QtWidgets.QPushButton()
        
        self.layout.addWidget(button1)
        self.layout.addWidget(button2)
        self.layout.addWidget(button3)
        
        print (self.frame.findChildren(QtWidgets.QPushButton, ''))

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    qtApp = TestWidget()
    qtApp.show()
    app.exec_()