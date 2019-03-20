'''
Created on Mar 8, 2019

@author: ajacobs
'''
import sys
import os



from dnd.player import Player

from PySide2.QtWidgets import *

app = QApplication(sys.argv)

class DnDWindow(QDialog):
    def __init__(self):
        super(DnDWindow, self).__init__()
        #DELETES THE UI WHEN CLOESED
        self.setAttribute(Qt.WA_DeleteOnClose)
        
        #BASIC UI PARAMATERS
        self.setWindowTitle('Character Sheet')
        self.setObjectName('CharacterSheetUI')
        #self.setMinimumSize(225, 550)
        #self.setMaximumSize(225, 550)
        self.resize(225, 550)
        
        self.Player=Player()
        self.buildLayout()
        
    def buildLayout(self):
        #Set up Abilities and features Layout
        self.afLayout=QVBoxLayout()
        self.afLayout.addWidget(StatsLayout(self.Player))
        self.afLayout.addWidget(SkillsLayout(self.Player))
        
        charSheetLayout=QHBoxLayout()
        charSheetLayout.addLayout(self.afLayout)
        
        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(10)
        mainLayout.contentsMargins()
        
        mainLayout.addWidget(CharBanner(self.Player))
        mainLayout.addLayout(charSheetLayout)
        
        self.setLayout(mainLayout)

'''Character banner UI elements'''       
class CharBanner(QDialog):
    def __init__(self, Player):
        super(CharBanner, self).__init__()
        self.Player=Player
        
        self.charInfoLayout=QVBoxLayout()
        self.charInfoLayout.setContentsMargins(0,0,0,0)
        self.charInfoLayout.setSpacing(0)
        
        self.layout=QHBoxLayout()
        self.layout.addWidget(CharAvatar())
        self.layout.addLayout(self.charInfoLayout)
        
        self.setLayout(self.layout)
        
        self.setBannerLayout()
        
    def setBannerLayout(self):
        self.charInfoLayout.addWidget(CharInfo(self.Player))
        self.charInfoLayout.addWidget(CharStats(self.Player))
        
class CharAvatar(QFrame):
    '''Sets up UI for the character avatar as well as the character level, race, and class level.'''
    def __init__(self):
        super(CharAvatar, self).__init__()
        self.Player=Player
        
        self.layout=QHBoxLayout()
        self.setLayout(self.layout)
        self.setAvatar()
        
    def setAvatar(self):
        '''Set up avatar and return the UI element'''
        avatarFilePath=r'C:\Users\ajacobs\Google Drive\DnD\binder\dnd.jpg'
        self.avatar = QLabel()
        self.avatar.setGeometry(0,0,100,100)
        self.avatar.setMaximumSize(100,100)
        self.avatar.setPixmap(QPixmap(avatarFilePath))
        self.layout.addWidget(self.avatar)
    
class CharInfo(QFrame):
    def __init__(self,Player):
        super(CharInfo, self).__init__()
        self.Player=Player
        
        self.classLvlLayout=QVBoxLayout()
        self.classLvlLayout.setSpacing(0)
        
        self.raceLayout=QVBoxLayout()
        self.raceLayout.setSpacing(0)
        
        self.charInfoLayout=QHBoxLayout()
        self.charInfoLayout.addLayout(self.raceLayout)
        self.charInfoLayout.addLayout(self.classLvlLayout)  
        
        self.layout=QHBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,15,0,0)
        self.layout.addLayout(self.charInfoLayout)
        
        self.setLayout(self.layout)
        
        self.setRaceLayout()
        self.setClassLvlLayout()
        
    def setRaceLayout(self):
        race='Hill Dwarf'
        
        self.raceLE=QLineEdit(race)
        self.raceLE.setMinimumWidth(70)
        raceLbl=QLabel('Race')
        
        self.raceLayout.addWidget(self.raceLE)
        self.raceLayout.addWidget(raceLbl)
    
    def setClassLvlLayout(self):
        classLvl='Blood Hunter 3 / Monk 1'
        
        self.classLvlLE=QLineEdit(classLvl)
        self.classLvlLE.setMinimumWidth(150)
        classLvlLbl=QLabel('Class & Level')
        
        self.classLvlLayout.addWidget(self.classLvlLE)
        self.classLvlLayout.addWidget(classLvlLbl)
        
class CharStats(QFrame):
    def __init__(self, Player):
        super(CharStats, self).__init__()
        self.Player=Player
        self.charStats={'PROFICIENCY BONUS':None, 'ARMOR CLASS':None, 'WALKING SPEED':None, 'PASSIVE PERCEPTION':None, 'INITIATIVE':None}
        
        self.layout=QHBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
       
        self.setLayout(self.layout)
        self.setStatLayout()
        
    def setStatLayout(self):
        for stat in self.charStats:
            statUI=CharStat(stat,self.Player)
            self.layout.addWidget(statUI)     
                
class CharStat(QFrame):
    def __init__(self, statType, Player):
        super(CharStat, self).__init__()
        self.Player=Player
        self.statType=statType
        
        self.statLayout=QHBoxLayout()
        self.statLayout.setSpacing(0)
        
        self.layout=QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.addLayout(self.statLayout)
        
        self.setLayout(self.layout)
        
        self.setStatLayout()
        self.addLabels()
    
    def setStatLayout(self):
        #Set up validator for inputs
        intVal=QIntValidator(0, 20)
        
        #Set inputbox size
        maxW=30
        maxH=30
        
        #Set font size
        font=QFont()
        font.setPointSize(15)
        
        spacerW=20
        spacerH=0
        spacer1=QSpacerItem(spacerW,spacerH)
        spacer2=QSpacerItem(spacerW,spacerH)
        
        self.statLE=QLineEdit()
        self.statLE.setMaximumSize(maxW,maxH)
        self.statLE.setMinimumSize(maxW,maxH)
        self.statLE.setValidator(intVal)
        self.statLE.setFont(font)
        
        self.statLayout.addSpacerItem(spacer1)
        self.statLayout.addWidget(self.statLE)
        self.statLayout.addSpacerItem(spacer2)
        
    def addLabels(self):
        if not self.statType=='INITIATIVE'>10:
            statType=self.statType.split(' ')
            statLbl1=QLabel(statType[0])
            statLbl1.setAlignment(Qt.AlignHCenter)
            statLbl2=QLabel(statType[1])
            statLbl2.setAlignment(Qt.AlignHCenter)
            self.layout.addWidget(statLbl1)
            self.layout.addWidget(statLbl2)
        else:
            statLbl=QLabel(self.statType)
            statLbl.setAlignment(Qt.AlignHCenter)
            self.layout.addWidget(statLbl)


'''UI section frame and layout class. To be called with each section so I can adjust any settings across the board'''
class SectionLayout(QVBoxLayout):
    def __init__(self):
        super(SectionLayout, self).__init__()
        self.setSpacing(0)
        

class SectionFrame(QFrame): 
    def __init__(self):
        super(SectionFrame, self).__init__()
        self.layout=SectionLayout()
        self.setLineWidth(1)
        self.setFrameStyle(QFrame.Box|QFrame.Sunken)  
        self.setLayout(self.layout)  


'''Stat layout and individual widget.'''
class StatsLayout(SectionFrame):
    '''Goes through the hard coded stats and builds out the substantiates the UI class for each one of them.'''
    def __init__(self, Player):
        super(StatsLayout, self).__init__()
        self.Player=Player
        self.statDict={'Strength':None, 'Dexterity':None, 'Constitution':None, 'Intelligence':None, 'Wisdom':None, 'Charisma':None}
        
        self.populateLayout()
        
    def populateLayout(self):
        for stat in self.statDict.keys():
            statUI=StatWidget(self.Player, stat)
            self.statDict[stat]=statUI
            self.layout.addWidget(statUI)    

class StatWidget(QWidget):
    '''Builds the individual UI for the stats. To be called by the StatsUI class. Any adjustments to the UI should
    be done here. I broke up the Stat and modifier/saves so each could be adjusted individually if needed.'''
    def __init__(self, Player, statName, value=None):
        super(StatWidget, self).__init__()
        
        self.Player=Player
        self.name=statName
        self.value=value
        
        self.layout=QHBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,5,0,0)
        self.setLayout(self.layout)
        
        self.setStatLayout()

    def setStatLayout(self):
        #Set up validator for inputs
        intVal=QIntValidator(0, 20)
        
        #Set inputbox size
        maxW=30
        maxH=30
        
        #Set font size
        font=QFont()
        font.setPointSize(15)
        
        #Set label for stat
        self.statLbl=QLabel(self.name)
        self.statLbl.setMinimumSize(80,20)
        
        #Set input box for stat
        self.statLE=QLineEdit()
        self.statLE.setMaximumSize(maxW,maxH)
        self.statLE.setMinimumSize(maxW,maxH)
        self.statLE.setValidator(intVal)
        self.statLE.setFont(font)
        
        self.statLE.editingFinished.connect(self.setStat)
        
        #Set up spacer between stat and Mod
        self.statSpacer=QSpacerItem(100,0)
        
        #Set up modifier laber
        self.modLbl=QLabel('Mod  ')
        self.modLbl.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        
        #Set up modifier input
        self.modLE=QLineEdit()
        self.modLE.setMaximumSize(maxW,maxH)
        self.modLE.setMinimumSize(maxW,maxH)
        self.modLE.setFont(font)
        self.modLE.setValidator(intVal)
        
        self.modLE.editingFinished.connect(self.getStat)
        
        #Set up spacer between modifier and save
        self.modSpacer=QSpacerItem(0,0)
        
        #Set up label for save
        self.saveLbl=QLabel('Save  ')
        self.saveLbl.setAlignment(Qt.AlignVCenter | Qt.AlignRight)
        
        #Set up input box for save
        self.saveLE=QLineEdit()
        self.saveLE.setMaximumSize(maxW,maxH)
        self.saveLE.setMinimumSize(maxW,maxH)
        self.saveLE.setFont(font)
        self.saveLE.setValidator(intVal)
        
        #Set up proficient checkbox
        self.profCheck=QCheckBox()
        
        #Set up layout for stat items and add them to layout
        self.statLayout=QHBoxLayout()
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
    
    def setStat(self):
        self.Player.setStat(self.name, self.statLE.text())
    
    def setModifier(self):
        #Get the modifier for the stat
        pass
    
    def getStat(self):
        #Get the stat number
        print self.Player.getStat('Strength')
        return self.statLE.text()
    
class StatWidget2(QWidget):
    def __init__(self):
        super(StatWidget2, self).__init__()
        
        self.statLayout=QVBoxLayout()
        
        self.modLayout=QVBoxLayout()
        
        self.saveLayout=QVBoxLayout()
        

class SkillsLayout(SectionFrame):
    '''Goes through the list of the hard coded skills and substantiates the UI class for each one of them.'''
    def __init__(self, Player):
        super(SkillsLayout, self).__init__()
        self.skillDict={'Acrobatics':None,'Animal Handling':None, 'Arcana':None, 'Athletics':None,
                        'Deception':None, 'History':None, 'Insight':None, 'Intimidation':None,
                        'Investigation':None, 'Medicine':None, 'Nature':None, 'Perception':None,
                        'Performance':None, 'Persuasion':None, 'Religion':None, 'Sleight of Hand':None,
                        'Stealth':None, 'Survival':None}
        
        self.Player=Player
        
        self.firstSkillLayout=QVBoxLayout()
        self.secondSkillLayout=QVBoxLayout()
        
        self.allSkillsLayout=QHBoxLayout()
        self.allSkillsLayout.addLayout(self.firstSkillLayout)
        self.allSkillsLayout.addLayout(self.secondSkillLayout)
        
        self.layout.addLayout(self.allSkillsLayout)
        
        self.populateUI()
        
    def populateUI(self):
        for skill in sorted(self.skillDict.keys()):
            skillUI=SkillUI(skill,self.Player)
            self.skillDict[skill]=skillUI
            if self.firstSkillLayout.count()==9:
                self.secondSkillLayout.addWidget(skillUI)
            else:
                self.firstSkillLayout.addWidget(skillUI)

class SkillUI(QFrame):
    def __init__(self, skillName, Player):
        '''Builds out the UI for the skills. To be called by the SkillsUI. I did this in order to be able to 
        make adjustments for them uniformily more easily.'''
        super(SkillUI, self).__init__()
        self.statToSkillDic={'Acrobatics':'DEX','Animal Handling':'WIS', 'Arcana':'INT', 'Athletics':'STR',
                        'Deception':'CHA', 'History':'INT', 'Insight':'WIS', 'Intimidation':'CHA',
                        'Investigation':'INT', 'Medicine':'WIS', 'Nature':'INT', 'Perception':'WIS',
                        'Performance':'CHA', 'Persuasion':'CHA', 'Religion':'INT', 'Sleight of Hand':'DEX',
                        'Stealth':'DEX', 'Survival':'WIS'}
        
        self.name=skillName
        self.Player=Player
        
        self.nameLayout=QHBoxLayout()
        
        self.skillLayout=QHBoxLayout()
        self.skillLayout.setSpacing(0)
        
        self.layout=QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(5,5,0,0)
        
        self.layout.setSpacing(0)
        
        self.setLayout(self.layout)
        
        self.setSkillLayout()
        
    def setSkillLayout(self):
        #Sets the skill and stat that goes with the skill layout so it can be adjusted separately from the input
        #Set up validator for inputs
        intVal=QIntValidator(0, 20)
        
        #Set inputbox size
        maxW=30
        maxH=30
        
        #Set font size
        font=QFont()
        font.setPointSize(15)
              
        #Set label for attr that controls the skill
        statLbl=QLabel(self.statToSkillDic[self.name])
        
        #Set up label for skill
        skillLbl=QLabel(self.name)
        skillLbl.setMinimumSize(80,0)
        
        #Set up proficient checkbox
        self.profChec=QCheckBox()
        
        #Set up input box for skill
        self.skillLE=QLineEdit()
        self.skillLE.setMaximumSize(maxW,maxH)
        self.skillLE.setMinimumSize(maxW,maxH)
        self.skillLE.setFont(font)
        self.skillLE.setValidator(intVal)
        
        self.skillLayout.addWidget(skillLbl)
        self.skillLayout.addWidget(self.profChec)
        self.skillLayout.addWidget(self.skillLE)
        
        self.layout.addWidget(statLbl)
        self.layout.addLayout(self.skillLayout)
        

GUI=DnDWindow()   
GUI.show()
sys.exit(app.exec_())            