'''
Created on Mar 8, 2019

@author: ajacobs
'''
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2.QtCore import Qt

from dnd.UI.util import SectionFrame

class Layout(SectionFrame):
    '''Goes through the list of the hard coded skills and substantiates the UI class for each one of them.'''
    def __init__(self, Player):
        super(Layout, self).__init__()
        self.skillDict={'Acrobatics':None,'Animal Handling':None, 'Arcana':None, 'Athletics':None,
                        'Deception':None, 'History':None, 'Insight':None, 'Intimidation':None,
                        'Investigation':None, 'Medicine':None, 'Nature':None, 'Perception':None,
                        'Performance':None, 'Persuasion':None, 'Religion':None, 'Sleight of Hand':None,
                        'Stealth':None, 'Survival':None}
        
        self.Player=Player
        
        self.firstSkillLayout=QtWidgets.QVBoxLayout()
        self.secondSkillLayout=QtWidgets.QVBoxLayout()
        
        self.allSkillsLayout=QtWidgets.QHBoxLayout()
        self.allSkillsLayout.addLayout(self.firstSkillLayout)
        self.allSkillsLayout.addLayout(self.secondSkillLayout)
        
        self.layout.addLayout(self.allSkillsLayout)
        
        self.populateUI()
        
    def populateUI(self):
        for skill in sorted(self.skillDict.keys()):
            skillUI=UI(skill,self.Player)
            self.skillDict[skill]=skillUI
            if self.firstSkillLayout.count()==9:
                self.secondSkillLayout.addWidget(skillUI)
            else:
                self.firstSkillLayout.addWidget(skillUI)

class UI(QtWidgets.QFrame):
    def __init__(self, skillName, Player):
        '''Builds out the UI for the skills. To be called by the SkillsUI. I did this in order to be able to 
        make adjustments for them uniformily more easily.'''
        super(UI, self).__init__()
        self.statToSkillDic={'Acrobatics':'DEX','Animal Handling':'WIS', 'Arcana':'INT', 'Athletics':'STR',
                        'Deception':'CHA', 'History':'INT', 'Insight':'WIS', 'Intimidation':'CHA',
                        'Investigation':'INT', 'Medicine':'WIS', 'Nature':'INT', 'Perception':'WIS',
                        'Performance':'CHA', 'Persuasion':'CHA', 'Religion':'INT', 'Sleight of Hand':'DEX',
                        'Stealth':'DEX', 'Survival':'WIS'}
        
        self.name=skillName
        self.Player=Player
        
        self.nameLayout=QtWidgets.QHBoxLayout()
        
        self.skillLayout=QtWidgets.QHBoxLayout()
        self.skillLayout.setSpacing(0)
        
        self.layout=QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(5,5,0,0)
        
        self.layout.setSpacing(0)
        
        self.setLayout(self.layout)
        
        self.setSkillLayout()
        
    def setSkillLayout(self):
        #Sets the skill and stat that goes with the skill layout so it can be adjusted separately from the input
        #Set up validator for inputs
        intVal=QtGui.QIntValidator(0, 20)
        
        #Set inputbox size
        maxW=30
        maxH=30
        
        #Set font size
        font=QtGui.QFont()
        font.setPointSize(15)
              
        #Set label for attr that controls the skill
        statLbl=QtWidgets.QLabel(self.statToSkillDic[self.name])
        
        #Set up label for skill
        skillLbl=QtWidgets.QLabel(self.name)
        skillLbl.setMinimumSize(80,0)
        
        #Set up proficient checkbox
        self.profChec=QtWidgets.QCheckBox()
        
        #Set up input box for skill
        self.skillLE=QtWidgets.QLineEdit()
        self.skillLE.setMaximumSize(maxW,maxH)
        self.skillLE.setMinimumSize(maxW,maxH)
        self.skillLE.setFont(font)
        self.skillLE.setValidator(intVal)
        
        self.skillLayout.addWidget(skillLbl)
        self.skillLayout.addWidget(self.profChec)
        self.skillLayout.addWidget(self.skillLE)
        
        self.layout.addWidget(statLbl)
        self.layout.addLayout(self.skillLayout)