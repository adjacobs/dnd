"""
Created on Mar 25, 2019

@author: ajacobs
"""
from PySide2 import QtCore, QtGui, QtWidgets


class Tab(QtWidgets.QTabWidget):
    def __init__(self):
        super(Tab, self).__init__()
        self.setGeometry(QtCore.QRect(170, 220, 351, 241))
        self.setObjectName("tabWidget")
        
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.addTab(self.tab, "")
        
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.addTab(self.tab_2, "")
        
        self.setCurrentIndex(0)
