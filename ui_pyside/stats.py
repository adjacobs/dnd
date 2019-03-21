'''
Created on Mar 8, 2019

@author: ajacobs
'''
from PySide2 import QtCore, QtGui, QtWidgets

class StatWidget(QtWidgets.QFrame):
    def __init__(self, stat, parent):
        super(StatWidget, self).__init__()
        self.Stat=stat
        self.Parent=parent
        
        #Setting paramaters for QFrame inherited class
        self.setGeometry(QtCore.QRect(420, 140, 164, 744))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setObjectName("statFrame")
        
        #Setting layout that frame uses
        self.statFrameVLayout = QtWidgets.QVBoxLayout(self)
        self.statFrameVLayout.setObjectName("statFrameVLayout")
        
        #Set shared font paramaters
        font = QtGui.QFont()
        font.setWeight(50)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        
        #Set up label including adding to layout
        self.statLabel = QtWidgets.QLabel(self)
        self.statLabel.setText(self.Stat.getName())
        self.statLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statLabel.setObjectName("statLabel")
        self.statFrameVLayout.addWidget(self.statLabel)
        
        #Spacers set up (Used for both value and modifier)
        leftSpacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        rightSpacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        #Set font size for value line edit
        font.setPointSize(22)
        
        #Setting up value line edit. Including layout and adding to the frame
        self.valueHLayout = QtWidgets.QHBoxLayout()
        self.valueHLayout.setObjectName("valueHLayout")
        self.valueHLayout.addItem(leftSpacerItem)
        self.valueLineEdit = QtWidgets.QLineEdit(self)
        self.valueLineEdit.setMinimumSize(QtCore.QSize(50, 50))
        self.valueLineEdit.setMaximumSize(QtCore.QSize(50, 50))
        self.valueLineEdit.setFont(font)
        self.valueLineEdit.setMaxLength(2)
        self.valueLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.valueLineEdit.setObjectName("valueLineEdit")
        
        #Set value line edit validator
        onlyInt=QtGui.QIntValidator(0, 40)
        self.valueLineEdit.setValidator(onlyInt)
        
        #Set value line edit value
        self.valueLineEdit.setText(str(self.Stat.get()))
        self.valueHLayout.addWidget(self.valueLineEdit)
        self.valueHLayout.addItem(rightSpacerItem)
        self.statFrameVLayout.addLayout(self.valueHLayout)
        
        #Set font size for modifier line edit
        font.setPointSize(14)
        
        #Setting up modifier line edit. Including layout and adding to the frame
        self.modHLayout = QtWidgets.QHBoxLayout()
        self.modHLayout.setObjectName("modHLayout")
        self.modHLayout.addItem(leftSpacerItem)
        self.modLineEdit = QtWidgets.QLineEdit(self)
        self.modLineEdit.setFont(font)
        self.modLineEdit.setMaxLength(2)
        self.modLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.modLineEdit.setMinimumSize(QtCore.QSize(30, 30))
        self.modLineEdit.setMaximumSize(QtCore.QSize(30, 30))
        self.modLineEdit.setObjectName("modLineEdit")
        self.modLineEdit.setReadOnly(True)
        
        #Set mod line edit value
        self.modLineEdit.setText(str(self.Stat.getModifier()))
        self.modHLayout.addWidget(self.modLineEdit)
        self.modHLayout.addItem(rightSpacerItem)
        self.statFrameVLayout.addLayout(self.modHLayout)
        
        #Connect value line edit function
        self.valueLineEdit.editingFinished.connect(self.setValue)       
    
    def setValue(self):
        '''Function to set value of stat as well as change modifier accordingly
        Can be set on the UI level'''
        inputValue=self.valueLineEdit.text()
        if inputValue != str(self.Stat.value):
            self.Stat.set(inputValue)
            self.modLineEdit.setText(str(self.Stat.getModifier()))
            self.Parent.refreshSkills()
    
    def refreshUI(self):
        '''refresh function that checks that stat widget number matches
        the corrisponding stat in the player class.'''
        self.valueLineEdit.setText(str(self.Stat.get()))
        self.modLineEdit.setText(str(self.Stat.getModifier()))
        