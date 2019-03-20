'''
Created on Mar 8, 2019

@author: ajacobs
'''
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2.QtCore import Qt

from PySide2.QtCore import QStringListModel

from dnd.UI.util import SectionFrame
        
class Widget(QtWidgets.QWidget):
    '''Builds the individual UI for the stats. To be called by the StatsUI class. Any adjustments to the UI should
    be done here. I broke up the Stat and modifier/saves so each could be adjusted individually if needed.'''
    def __init__(self, Stat):
        super(Widget, self).__init__()
        self.stat=Stat
        
        self.layout=QtWidgets.QHBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,5,0,0)
        self.setLayout(self.layout)
        self.setStatLayout()
    
    def setStatLayout(self):
        #Set up validator for inputs
        intVal=QtGui.QIntValidator(0, 20)
        
        #Set inputbox size
        maxW=30
        maxH=30
        
        #Set font size
        font=QtGui.QFont()
        font.setPointSize(15)
        
        #Set label for stat
        self.statLbl=QtWidgets.QLabel(self.stat.name)
        self.statLbl.setMinimumSize(80,20)
        
        #Set input box for stat
        self.statLE=QtWidgets.QLineEdit()
        self.statLE.setMaximumSize(maxW,maxH)
        self.statLE.setMinimumSize(maxW,maxH)
        self.statLE.setValidator(intVal)
        self.statLE.setFont(font)
        
        #Set up spacer between stat and Mod
        self.statSpacer=QtWidgets.QSpacerItem(100,0)
        
        #Set up modifier laber
        self.modLbl=QtWidgets.QLabel('Mod  ')
        self.modLbl.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        
        #Set up modifier input
        self.modLE=QtWidgets.QLineEdit()
        self.modLE.setMaximumSize(maxW,maxH)
        self.modLE.setMinimumSize(maxW,maxH)
        self.modLE.setFont(font)
        self.modLE.setValidator(intVal)
        
        #Set up spacer between modifier and save
        self.modSpacer=QtWidgets.QSpacerItem(0,0)
        
        #Set up label for save
        self.saveLbl=QtWidgets.QLabel('Save  ')
        self.saveLbl.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        
        #Set up input box for save
        self.saveLE=QtWidgets.QLineEdit()
        self.saveLE.setMaximumSize(maxW,maxH)
        self.saveLE.setMinimumSize(maxW,maxH)
        self.saveLE.setFont(font)
        self.saveLE.setValidator(intVal)
        
        #Set up proficient checkbox
        self.profCheck=QtWidgets.QCheckBox()
        
        #Set up layout for stat items and add them to layout
        self.statLayout=QtWidgets.QHBoxLayout()
        self.statLayout.addWidget(self.statLbl)
        self.statLayout.addWidget(self.statLE)
        #self.statLayout.addSpacerItem(self.statSpacer)
        self.statLayout.addWidget(self.modLbl)
        self.statLayout.addWidget(self.modLE)
        #self.statLayout.addSpacerItem(self.modSpacer)
        self.statLayout.addWidget(self.saveLbl)
        self.statLayout.addWidget(self.saveLE)
        self.statLayout.addWidget(self.profCheck)
        
        #AddStat layout to main layout
        self.layout.addLayout(self.statLayout)
    
    def connectWidget(self):
        self.statLE.editingFinished.connect(self.setStat)
        self.modLE.editingFinished.connect(self.getStat)
        
    def setStat(self):
        self.stat.set(self.statLE.text())
    
    def setModifier(self):
        #Get the modifier for the stat
        pass
    
    def getStat(self):
        #Get the stat number
        print (self.name)
        return self.statLE.text()
    
'''Stat frame widget. Inherits from UI.util. Takes in stat list and builds out 
   widget for stat input'''
class FrameWidget(SectionFrame):
    def __init__(self, Stats):
        super(FrameWidget, self).__init__()
        for stat in Stats:
            statUI=Widget(stat)
            self.layout.addWidget(statUI) 
