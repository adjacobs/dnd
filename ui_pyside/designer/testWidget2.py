# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ajacobs\Python\tools\dnd\UI\resources\\testWidget2.ui',
# licensing of 'C:\Users\ajacobs\Python\tools\dnd\UI\resources\\testWidget2.ui' applies.
#
# Created: Fri Mar 15 11:41:08 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menudropDown = QtWidgets.QMenu(self.menubar)
        self.menudropDown.setObjectName("menudropDown")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondropDownItem = QtWidgets.QAction(MainWindow)
        self.actiondropDownItem.setObjectName("actiondropDownItem")
        self.menudropDown.addAction(self.actiondropDownItem)
        self.menubar.addAction(self.menudropDown.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.menudropDown.setTitle(QtWidgets.QApplication.translate("MainWindow", "dropDown", None, -1))
        self.actiondropDownItem.setText(QtWidgets.QApplication.translate("MainWindow", "dropDownItem", None, -1))

