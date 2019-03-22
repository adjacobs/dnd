'''
Created on Mar 21, 2019

@author: ajacobs
'''
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QPushButton

class DetailsWidget(QtWidgets.QFrame):
    def __init__(self):
        super(DetailsWidget, self).__init__()
        
        '''Builds Frame for stat widgets to get added to and adds the frame to the central widget'''
        #Setting up frame pramaters
        self.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setObjectName("specsFrame")
        
        #self.setMaximumWidth(100)
        
        #Setting frame layout for stat widgets to be added to
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setObjectName("specsLayout")
        
        self.layout.addWidget(CombatFrame())
        self.layout.addWidget(HealthFrame())

class CombatFrame(QtWidgets.QFrame):
    def __init__(self):
        super(CombatFrame, self).__init__()
        
        '''Builds Frame for stat widgets to get added to and adds the frame to the central widget'''
        #Setting up frame pramaters
        self.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setObjectName("combatFrame")
        
        #self.setMaximumWidth(100)
        
        #Setting frame layout for stat widgets to be added to
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setObjectName("combatLayout")
        
        self.minSize=QtCore.QSize(50, 50)
        self.maxSize=QtCore.QSize(50, 50)
        self.allignment=QtCore.Qt.AlignCenter
        
        self.font=QtGui.QFont()
        self.font.setWeight(50)
        self.font.setUnderline(False)
        self.font.setStrikeOut(False)
        self.font.setBold(False)
        
        self.buildACFrame()
        self.buildSpeedFrame()
        self.buildInitiativeFrame()
        
    def buildACFrame(self):
        self.acFrame=QtWidgets.QFrame()
        self.acFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.acFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.acFrame.setObjectName("acFrame")
        
        self.acLayout=QtWidgets.QVBoxLayout(self.acFrame)
        self.acLayout.setObjectName('acLayout')
        
        self.acLineEdit=QtWidgets.QLineEdit()
        self.acLineEdit=QtWidgets.QLineEdit()
        self.acLineEdit.setMinimumSize(self.minSize)
        self.acLineEdit.setMaximumSize(self.maxSize)
        self.acLineEdit.setFont(self.font)
        self.acLineEdit.setAlignment(self.allignment)
        
        self.acLabel=QtWidgets.QLabel('Armor Class')
        
        self.acLayout.addWidget(self.acLineEdit)
        self.acLayout.addWidget(self.acLabel)
        
        self.layout.addWidget(self.acFrame)
        
    def buildSpeedFrame(self):
        self.speedFrame=QtWidgets.QFrame()
        self.speedFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.speedFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.speedFrame.setObjectName("speedFrame")
        
        self.speedLayout=QtWidgets.QVBoxLayout(self.speedFrame)
        self.speedLayout.setObjectName('speedLayout')
        
        self.speedLineEdit=QtWidgets.QLineEdit()
        self.speedLineEdit.setMinimumSize(self.minSize)
        self.speedLineEdit.setMaximumSize(self.maxSize)
        self.speedLineEdit.setFont(self.font)
        self.speedLineEdit.setAlignment(self.allignment)
        
        self.speedLabel=QtWidgets.QLabel('Speed')
        
        self.speedLayout.addWidget(self.speedLineEdit)
        self.speedLayout.addWidget(self.speedLabel)
        
        self.layout.addWidget(self.speedFrame)
        
    def buildInitiativeFrame(self):
        self.initiativeFrame=QtWidgets.QFrame()
        self.initiativeFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.initiativeFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.initiativeFrame.setObjectName("initiativeFrame")
        
        self.initiativeLayout=QtWidgets.QVBoxLayout(self.initiativeFrame)
        self.initiativeLayout.setObjectName('initiativeLayout')
        
        self.initiativeLineEdit=QtWidgets.QLineEdit()
        self.initiativeLineEdit.setMinimumSize(self.minSize)
        self.initiativeLineEdit.setMaximumSize(self.maxSize)
        self.initiativeLineEdit.setFont(self.font)
        self.initiativeLineEdit.setAlignment(self.allignment)
        
        self.initiativeLabel=QtWidgets.QLabel('Initiative')
        
        self.initiativeLayout.addWidget(self.initiativeLineEdit)
        self.initiativeLayout.addWidget(self.initiativeLabel)
        
        self.layout.addWidget(self.initiativeFrame)

class HealthFrame(QtWidgets.QFrame):
    def __init__(self):
        super(HealthFrame, self).__init__()
        
        '''Builds Frame for stat widgets to get added to and adds the frame to the central widget'''
        #Setting up frame pramaters
        self.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setObjectName("healthFrame")
        
        #self.setMaximumWidth(100)
        
        #Setting frame layout for stat widgets to be added to
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setObjectName("combatSpecsLayout")
        
        self.minSize=QtCore.QSize(50, 50)
        self.maxSize=QtCore.QSize(50, 50)
        self.allignment=QtCore.Qt.AlignCenter
        
        self.font=QtGui.QFont()
        self.font.setWeight(50)
        self.font.setUnderline(False)
        self.font.setStrikeOut(False)
        self.font.setBold(False)
        
        self.buildHealthFrame()
        self.buildTempHealthFrame()
        
    def buildHealthFrame(self):
        self.healthFrame=QtWidgets.QFrame()
        self.healthFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.healthFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.healthFrame.setObjectName("healthFrame")
        
        self.healthLayout=QtWidgets.QHBoxLayout(self.healthFrame)
        self.healthLayout.setObjectName('healthLayout')
        
        self.minusHealthButton=QtWidgets.QPushButton("-")
        
        self.healthLineEdit=QtWidgets.QLineEdit()
        self.healthLineEdit.setMinimumSize(QtCore.QSize(50, 50))
        self.healthLineEdit.setMaximumSize(QtCore.QSize(50, 50))
        self.healthLineEdit.setFont(self.font)
        self.healthLineEdit.setMaxLength(2)
        self.healthLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        
        self.addHealthButton=QtWidgets.QPushButton("+")
        
        self.healthLayout.addWidget(self.minusHealthButton)
        self.healthLayout.addWidget(self.healthLineEdit)
        self.healthLayout.addWidget(self.addHealthButton)
        
        self.layout.addWidget(self.healthFrame)
    
    def buildTempHealthFrame(self):
        self.tempHealthFrame=QtWidgets.QFrame()
        self.tempHealthFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.tempHealthFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tempHealthFrame.setObjectName("tempHealthFrame")
        
        self.tempHealthLayout=QtWidgets.QHBoxLayout(self.tempHealthFrame)
        self.tempHealthLayout.setObjectName('tempHealthLayout')
        
        self.minusTempHealthButton=QtWidgets.QPushButton("-")
        
        self.tempHealthLineEdit=QtWidgets.QLineEdit()
        self.tempHealthLineEdit.setMinimumSize(QtCore.QSize(50, 50))
        self.tempHealthLineEdit.setMaximumSize(QtCore.QSize(50, 50))
        self.tempHealthLineEdit.setFont(self.font)
        self.tempHealthLineEdit.setMaxLength(2)
        self.tempHealthLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        
        self.addTempHealthButton=QtWidgets.QPushButton("+")
        
        self.tempHealthLayout.addWidget(self.minusTempHealthButton)
        self.tempHealthLayout.addWidget(self.tempHealthLineEdit)
        self.tempHealthLayout.addWidget(self.addTempHealthButton)
        
        self.layout.addWidget(self.tempHealthFrame)
        
        