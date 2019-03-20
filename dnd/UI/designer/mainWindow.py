# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ajacobs\Python\tools\dnd\UI\resources\mainWindow.ui',
# licensing of 'C:\Users\ajacobs\Python\tools\dnd\UI\resources\mainWindow.ui' applies.
#
# Created: Wed Mar 13 16:02:09 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class UI(QtWidgets.QMainWindow):
    def __init__(self, MainWindow):
        super(UI, self).__init__()
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 1051)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))

