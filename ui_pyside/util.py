'''
Created on Mar 8, 2019

@author: ajacobs
'''
from PySide2 import QtCore, QtGui, QtWidgets

class VFrameWidget(QtWidgets.QFrame):
    def __init__(self, name):
        super(VFrameWidget, self).__init__()
        
        self.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setObjectName(name)
        
        #Setting layout that frame uses
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setObjectName("VLayout")
        
class HFrameWidget(QtWidgets.QFrame):
    def __init__(self, name):
        super(HFrameWidget, self).__init__()
        
        self.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setObjectName(name)
        
        #Setting layout that frame uses
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setObjectName("HLayout")