# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ajacobs\Python\tools\dnd\UI\resources\statWidget.ui',
# licensing of 'C:\Users\ajacobs\Python\tools\dnd\UI\resources\statWidget.ui' applies.
#
# Created: Wed Mar 13 15:43:55 2019
#      by: pyside2-uic  running on PySide2 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 1051)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.statFrame = QtWidgets.QFrame(self.centralwidget)
        self.statFrame.setGeometry(QtCore.QRect(420, 140, 164, 744))
        self.statFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.statFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.statFrame.setObjectName("statFrame")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.statFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
       
        self.statLabel = QtWidgets.QLabel(self.statFrame)
        self.statLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statLabel.setObjectName("statLabel")
        self.verticalLayout_2.addWidget(self.statLabel)
        
        self.valueHLayout = QtWidgets.QHBoxLayout()
        self.valueHLayout.setObjectName("valueHLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.valueHLayout.addItem(spacerItem)
        self.value_LE_3 = QtWidgets.QLineEdit(self.statFrame)
        self.value_LE_3.setMinimumSize(QtCore.QSize(40, 40))
        self.value_LE_3.setMaximumSize(QtCore.QSize(50, 50))
        self.value_LE_3.setObjectName("value_LE_3")
        self.valueHLayout.addWidget(self.value_LE_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.valueHLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.valueHLayout)
        self.modHLayout = QtWidgets.QHBoxLayout()
        self.modHLayout.setObjectName("modHLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.modHLayout.addItem(spacerItem2)
        self.modLineEdit = QtWidgets.QLineEdit(self.statFrame)
        self.modLineEdit.setMinimumSize(QtCore.QSize(30, 30))
        self.modLineEdit.setMaximumSize(QtCore.QSize(30, 30))
        self.modLineEdit.setObjectName("modLineEdit")
        self.modHLayout.addWidget(self.modLineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.modHLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.modHLayout)
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
        self.statLabel.setText(QtWidgets.QApplication.translate("MainWindow", "TextLabel", None, -1))

