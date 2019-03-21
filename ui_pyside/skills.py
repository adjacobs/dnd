'''
Created on Mar 8, 2019

@author: ajacobs
'''
from PySide2 import QtCore, QtGui, QtWidgets


class SkillWidget(QtWidgets.QFrame):
    def __init__(self, skill, parent):
        super(SkillWidget, self).__init__()
        self.Skill=skill
        self.Parent=parent
        
        #Setting paramaters for QFrame inherited class
        self.setGeometry(QtCore.QRect(420, 140, 164, 744))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setObjectName("skillFrame")
        
        #Setting layout that frame uses
        self.skillFrameHLayout = QtWidgets.QHBoxLayout(self)
        self.skillFrameHLayout.setObjectName("baseVerticalLayout")
        
        #Set shared font paramaters
        font = QtGui.QFont()
        font.setWeight(50)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        
        #Set font size for modifier line edit
        font.setPointSize(8)
        
        #Setting up proficiency line edit. Including layout and adding to the frame
        self.profLineEdit = QtWidgets.QLineEdit(self)
        self.profLineEdit.setMinimumSize(QtCore.QSize(15, 15))
        self.profLineEdit.setMaximumSize(QtCore.QSize(15, 15))
        self.profLineEdit.setFont(font)
        self.profLineEdit.setMaxLength(2)
        self.profLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.profLineEdit.setObjectName("valueLineEdit")
        self.skillFrameHLayout.addWidget(self.profLineEdit)
        
        #Set font size for value line edit
        font.setPointSize(10)
        
        #Setting up modifier line edit. Including layout and adding to the frame
        self.modLineEdit = QtWidgets.QLineEdit(self)
        self.modLineEdit.setMinimumSize(QtCore.QSize(20, 20))
        self.modLineEdit.setMaximumSize(QtCore.QSize(20, 20))
        self.modLineEdit.setFont(font)
        self.modLineEdit.setMaxLength(2)
        self.modLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.modLineEdit.setObjectName("modLineEdit")
        self.skillFrameHLayout.addWidget(self.modLineEdit)
        
        #Set up label including adding to layout
        self.skillLabel = QtWidgets.QLabel(self)
        self.skillLabel.setText(self.Skill.getName(stat=True))
        self.skillLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.skillLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.skillLabel.setObjectName("skillLabel")
        self.skillFrameHLayout.addWidget(self.skillLabel)
        
        #Set default for modifier
        self.setModifier()
        
        self.connectInputs()
        
    def connectInputs(self):
        '''Connects the finished edit signal to the functions'''
        self.profLineEdit.editingFinished.connect(self.valueFunction)
        self.modLineEdit.editingFinished.connect(self.modFunction)
    
    '''Test functions to be deleted before final set up'''
    def valueFunction(self):
        print('skille Value')
    
    def modFunction(self):
        print('skill mod')
        
    def setModifier(self):
        '''Sets the modifier value.'''
        self.modLineEdit.setText(str(self.Skill.getModifier()))
    
    def test(self):
        print ('Skills')
        
