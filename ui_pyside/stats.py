'''
Created on Mar 28, 2019

@author: ajacobs
'''
from PySide2 import QtCore, QtGui, QtWidgets
from dnd.engine.player import Player

class StatsWidget(QtWidgets.QFrame):
    def __init__(self, Player):
        super(StatsWidget, self).__init__()
        
        '''Builds Frame for stat widgets to get added to and adds the frame to the central widget'''
        #Setting up frame pramaters
        self.setGeometry(QtCore.QRect(260, 100, 184, 641))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("statsFrame")
        
        self.setMaximumWidth(200)
        
        #Setting frame layout for stat widgets to be added to
        self.statsFrameVLayout = QtWidgets.QVBoxLayout(self)
        self.statsFrameVLayout.setSpacing(2)
        self.statsFrameVLayout.setContentsMargins(1,1,1,1)
        self.statsFrameVLayout.setObjectName("statsFrameVLayout")
        
        #Go through the player stats and build out a frame widget for each
        #Passing in "self" so stat widgets can all refresh together
        for stat in Player.getStats():
            skills = Player.getSkills(byStat=True)
            self.statsFrameVLayout.addWidget(StatWidget(stat, skills[stat.getName()]))

class StatWidget(QtWidgets.QFrame):
    def __init__(self, stat, skills):
        super(StatWidget, self).__init__()
        self.Stat=stat
        self.Skills=[]

        #Setting paramaters for QFrame inherited class
        self.setGeometry(QtCore.QRect(50, 50, 50, 50))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setObjectName("mainFrame")
        
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.mainLayout.setContentsMargins(2,2,2,2)
        self.mainLayout.setSpacing(1)
        self.mainLayout.setObjectName("mainVLayout")
        
        #Set font class for UI
        #Set shared font paramaters
        self.font = QtGui.QFont()
        self.font.setWeight(50)
        self.font.setUnderline(False)
        self.font.setStrikeOut(False)
        self.font.setBold(False)
        
        self._buildStatFrame()
        self._buildSaveFrame()
        
        for skill in skills:
            widget=SkillWidget(skill)
            self.mainLayout.addWidget(widget)
            self.Skills.append(widget)
    
    def _buildStatFrame(self):
        #Set variables for size adjustment
        valueFont=10
        modFont=18
        statSize=QtCore.QSize(20, 20)
        modSize=QtCore.QSize(30, 30)
        layoutMargin = QtCore.QMargins(2,1,1,1)
        
        #Set up frame for stat
        self.statFrame=QtWidgets.QFrame()
        self.statFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.statFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.statFrame.setObjectName("statFrame")
        self.mainLayout.addWidget(self.statFrame)
        
        #Setting layout that frame uses
        self.statFrameVLayout = QtWidgets.QHBoxLayout(self.statFrame)
        self.statFrameVLayout.setObjectName("statFrameVLayout")
        self.statFrameVLayout.setContentsMargins(layoutMargin)
        
        #Set up label including adding to layout
        self.statLabel = QtWidgets.QLabel(self)
        self.statLabel.setText(self.Stat.getName())
        self.statLabel.setFont(self.font)
        self.statLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.statLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statLabel.setObjectName("statLabel")
        self.statFrameVLayout.addWidget(self.statLabel)
        
        #Spacers set up (Used for both value and modifier)
        leftSpacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        #Setting up value line edit. Including layout and adding to the frame
        self.font.setPointSize(valueFont)
        self.valueHLayout = QtWidgets.QHBoxLayout()
        self.valueHLayout.setObjectName("valueHLayout")
        self.valueHLayout.addItem(leftSpacerItem)
        self.valueLineEdit = QtWidgets.QLineEdit(self)
        self.valueLineEdit.setMinimumSize(statSize)
        self.valueLineEdit.setMaximumSize(statSize)
        self.valueLineEdit.setFont(self.font)
        self.valueLineEdit.setMaxLength(2)
        self.valueLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.valueLineEdit.setObjectName("valueLineEdit")
        
        #Set value line edit validator
        onlyInt=QtGui.QIntValidator(0, 40)
        self.valueLineEdit.setValidator(onlyInt)
        
        #Set value line edit value
        self.valueLineEdit.setText(str(self.Stat.get()))
        self.valueHLayout.addWidget(self.valueLineEdit)
        self.statFrameVLayout.addLayout(self.valueHLayout)
        
        #Setting up modifier line edit. Including layout and adding to the frame
        self.font.setPointSize(modFont)
        self.modHLayout = QtWidgets.QHBoxLayout()
        self.modHLayout.setObjectName("modHLayout")
        self.modHLayout.addItem(leftSpacerItem)
        self.modLineEdit = QtWidgets.QLineEdit(self)
        self.modLineEdit.setFont(self.font)
        self.modLineEdit.setMaxLength(2)
        self.modLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.modLineEdit.setMinimumSize(modSize)
        self.modLineEdit.setMaximumSize(modSize)
        self.modLineEdit.setObjectName("modLineEdit")
        self.modLineEdit.setReadOnly(True)
        
        #Set mod line edit value
        self.modLineEdit.setText(str(self.Stat.getModifier()))
        self.modHLayout.addWidget(self.modLineEdit)
        self.statFrameVLayout.addLayout(self.modHLayout)
        
        #Connect value line edit function
        self.valueLineEdit.editingFinished.connect(self.setValue)
    
    def _buildSaveFrame(self):
        #Set variables for size adjustment
        profSize = QtCore.QSize(10, 10)
        modSize = QtCore.QSize(20, 20)
        layoutMargin = QtCore.QMargins(5,0,15,0)
        self.font.setPointSize(10)
        
        #Set up frame for stat
        self.saveFrame=QtWidgets.QFrame()
        self.saveFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.saveFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.saveFrame.setObjectName("saveFrame")
        self.mainLayout.addWidget(self.saveFrame)
        
        #Setting layout that frame uses
        saveFrameHLayout = QtWidgets.QHBoxLayout(self.saveFrame)
        saveFrameHLayout.setObjectName("saveFrameVLayout")
        saveFrameHLayout.setContentsMargins(layoutMargin)
        
        #Set prof/expert line edit including adding to layout
        self.profLineEdit = QtWidgets.QLineEdit(self)
        self.profLineEdit.setFont(self.font)
        self.profLineEdit.setMaxLength(2)
        self.profLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.profLineEdit.setMinimumSize(profSize)
        self.profLineEdit.setMaximumSize(profSize)
        self.profLineEdit.setObjectName("saveProfLineEdit")
        self.profLineEdit.setReadOnly(True)
        saveFrameHLayout.addWidget(self.profLineEdit)
        
        #Set up label including adding to layout
        self.Label = QtWidgets.QLabel(self)
        self.Label.setText('Save')
        self.Label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Label.setObjectName("self.Label")
        saveFrameHLayout.addWidget(self.Label)
        
        #Set up modifier line edit including adding to layout
        self.saveModLineEdit = QtWidgets.QLineEdit(self)
        self.saveModLineEdit.setFont(self.font)
        self.saveModLineEdit.setMaxLength(2)
        self.saveModLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.saveModLineEdit.setMinimumSize(modSize)
        self.saveModLineEdit.setMaximumSize(modSize)
        self.saveModLineEdit.setObjectName("modLineEdit")
        self.saveModLineEdit.setReadOnly(True)
        saveFrameHLayout.addWidget(self.saveModLineEdit)
    
    def setValue(self):
        '''Function to set value of stat as well as change modifier accordingly
        Can be set on the UI level'''
        inputValue=self.valueLineEdit.text()
        if inputValue != str(self.Stat.value):
            self.Stat.set(inputValue)
            self.modLineEdit.setText(str(self.Stat.getModifier()))
            for skill in self.Skills:
                skill.update()
    
    def refreshUI(self):
        '''refresh function that checks that stat widget number matches
        the corrisponding stat in the player class.'''
        self.valueLineEdit.setText(str(self.Stat.get()))
        self.modLineEdit.setText(str(self.Stat.getModifier()))

class SkillWidget(QtWidgets.QFrame):
    def __init__(self, skill):
        super(SkillWidget, self).__init__()
        self.Skill=skill
        
        #Set shared font paramaters
        font = QtGui.QFont()
        font.setWeight(50)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        
        #Set variables for size adjustment
        font.setPointSize(10)
        profSize = QtCore.QSize(10, 10)
        modSize = QtCore.QSize(20, 20)
        layoutMargin = QtCore.QMargins(5,0,15,0)
        
        #Set up frame for stat
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("skillFrame")
        
        #Setting layout that frame uses
        skillFrameHLayout = QtWidgets.QHBoxLayout(self)
        skillFrameHLayout.setObjectName("skillFrameVLayout")
        skillFrameHLayout.setContentsMargins(layoutMargin)
        
        #Set prof/expert line edit including adding to layout
        self.profLineEdit = QtWidgets.QLineEdit(self)
        self.profLineEdit.setFont(font)
        self.profLineEdit.setMaxLength(2)
        self.profLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.profLineEdit.setMinimumSize(profSize)
        self.profLineEdit.setMaximumSize(profSize)
        self.profLineEdit.setObjectName("profLineEdit")
        self.profLineEdit.setReadOnly(True)
        skillFrameHLayout.addWidget(self.profLineEdit)
        
        #Set up label including adding to layout
        skillLabel = QtWidgets.QLabel(self)
        skillLabel.setText(skill.getName())
        skillLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        skillLabel.setAlignment(QtCore.Qt.AlignCenter)
        skillLabel.setObjectName("skillLabel")
        skillFrameHLayout.addWidget(skillLabel)
        
        #Set up modifier line edit including adding to layout
        self.modLineEdit = QtWidgets.QLineEdit(self)
        self.modLineEdit.setFont(font)
        self.modLineEdit.setMaxLength(2)
        self.modLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.modLineEdit.setMinimumSize(modSize)
        self.modLineEdit.setMaximumSize(modSize)
        self.modLineEdit.setObjectName("modLineEdit")
        self.modLineEdit.setReadOnly(True)
        skillFrameHLayout.addWidget(self.modLineEdit)
        
        self.update()
    
    def update(self):
        self.modLineEdit.setText(str(self.Skill.getModifier()))

'''
import sys        
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
layout = QtWidgets.QVBoxLayout(window)
layout.addWidget(StatsWidget(Player()))
window.show()
sys.exit(app.exec_())
'''
        