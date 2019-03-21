

from PySide2 import QtCore, QtGui, QtWidgets

#Import of UI elemenets
from dnd.ui_pyside.stats import StatsWidget
from dnd.ui_pyside.skills import SkillWidget
from dnd.ui_pyside.util import VFrameWidget, HFrameWidget

from PySide2.QtWidgets import QWidget

class UI(QtWidgets.QMainWindow):
    def __init__(self, playerEngine):
        super(UI, self).__init__()
        
        #Setting playerEnding to class variable
        self.Player = playerEngine()
        
        self.setObjectName("MainWindow")
        self.resize(836, 1051)

        #Set up central widget for the main window that allows other widgets to be added to.
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        
        #Sets up central widget layout for central widget that all UI elements will be added to
        self.centralVLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.centralVLayout.setObjectName("centralGLayout")
        
        
        '''Menu stuff. Not needed for a bit.
        #Set up menu par paramaters
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 21))
        self.menubar.setObjectName("menubar")
        
        #Set up drop down menu
        self.dropDownMenu = QtWidgets.QMenu(self.menubar)
        self.dropDownMenu.setObjectName('dropDownMenu')
        
        #Add menubar to Main Window
        self.setMenuBar(self.menubar)
        
        #Build drop down item and connect to function
        self.dropDownMenuItem = QtWidgets.QAction(self)
        self.dropDownMenuItem.setObjectName("dropDownMenuItem")
        self.dropDownMenuItem.triggered.connect(self.Player.testFunction)
        
        #Adds drop down menu to menu
        self.dropDownMenu.addAction(self.dropDownMenuItem)
        self.menubar.addAction(self.dropDownMenu.menuAction())
        
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        '''
        
        #Adding UI elements
        self.setBannerLayout()
        self.setChracterLayout()
        #self.addSkills()
        
    def retranslateUi(self):
        self.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "DnDWindow", None, -1))
        self.dropDownMenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "dropDownMenu", None, 1))
        self.dropDownMenuItem.setText(QtWidgets.QApplication.translate("MainWindow", "dropDownMenuItem", None, -1))
    
    '''Sets up title widget and layout'''
    def setBannerLayout(self):
        #Setting up frame pramaters
        self.bannerFrame = HFrameWidget('Banner')
        self.bannerFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bannerFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        
        #Adding frame to central layout
        self.centralVLayout.addWidget(self.bannerFrame)        
        
        self.avatarLayout=HFrameWidget('avatar')
        self.chrInfoLayout=HFrameWidget('info')
        
        self.bannerFrame.layout.addWidget(self.avatarLayout)
        self.bannerFrame.layout.addWidget(self.chrInfoLayout)
        
    def setChracterLayout(self):
        #Setting up frame pramaters
        self.characterFrame = HFrameWidget('character')
        self.characterFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.characterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        
        #Adding frame to central layout
        self.centralVLayout.addWidget(self.characterFrame)        
        
        self.statsWidget=StatsWidget(self.Player, self)
        self.chrOverviewWidget=VFrameWidget('overview')
        
        self.characterFrame.layout.addWidget(self.statsWidget)
        self.characterFrame.layout.addWidget(self.chrOverviewWidget)
        
        self.setCharacterDetailsLayout()
        
    def setCharacterDetailsLayout(self):
        self.characteSpecs=HFrameWidget('Specs')
        
        self.characterDetailsFrame=HFrameWidget('details')
        self.characterEquipmentFrame=HFrameWidget('equipment')
        
        self.chracterMenu=HFrameWidget('menu')
        
        self.chrOverviewWidget.layout.addWidget(self.characteSpecs)
        self.chrOverviewWidget.layout.addWidget(self.chracterMenu)
        
        self.characteSpecs.layout.addWidget(self.characterDetailsFrame)
        self.characteSpecs.layout.addWidget(self.characterEquipmentFrame)
    
    def addSkills(self):
        '''Builds Frame for skills widgets to get added to and adds the frame to the central widget'''
        #Setting up frame pramaters
        self.skillsFrame = QtWidgets.QFrame(self.centralwidget)
        self.skillsFrame.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.skillsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.skillsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.skillsFrame.setObjectName("skillsFrame")
        
        #Adding frame to central layout
        self.centralVLayout.addWidget(self.skillsFrame)
        
        #Setting frame layout for skills to be added to
        self.skillsFrameVLayout = QtWidgets.QVBoxLayout(self.skillsFrame)
        self.skillsFrameVLayout.setObjectName("skillsFrameVLayout")
        
        #Go through the player skills and build out a frame widget for each
        #Passing in "self" so stat widgets can all refresh together
        for skill in self.Player.getSkills():
            self.skillsFrameVLayout.addWidget(SkillWidget(skill, self))
    
    def refreshSkills(self):
        '''Goes through skill widgets and makes sure that the visual matches what the Player class has.'''
        for skill in self.skillsFrame.findChildren(QtWidgets.QFrame, 'skillFrame'):
            skill.setModifier()
