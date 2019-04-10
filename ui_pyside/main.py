

from PySide2 import QtCore, QtGui, QtWidgets

#Import of UI elemenets

from dnd.ui_pyside.details import DetailsWidget
from dnd.ui_pyside.tab import Tab

from dnd.ui_pyside.stats import ChrStatsWidget
from dnd.ui_pyside.traits import Traits
from dnd.ui_pyside.title import Title
from dnd.ui_pyside.util import FrameWidget

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

        #Adding UI elements
        self.centralVLayout.addWidget(Banner(self.Player))
        self.centralVLayout.addWidget(ChrOverView(self.Player))
        
    def retranslateUi(self):
        self.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "DnDWindow", None, -1))
        self.dropDownMenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "dropDownMenu", None, 1))
        self.dropDownMenuItem.setText(QtWidgets.QApplication.translate("MainWindow", "dropDownMenuItem", None, -1))
    
    def refreshSkills(self):
        '''Goes through skill widgets and makes sure that the visual matches what the Player class has.'''
        for skill in self.skillsFrame.findChildren(QtWidgets.QFrame, 'skillFrame'):
            skill.setModifier()
            
class Banner(FrameWidget):
    def __init__(self, Player):
        super(Banner, self).__init__(layoutType='H')
        self.layout.addWidget(Title(Player))
        self.layout.addWidget(Traits(Player))
        
class ChrOverView(FrameWidget):
    def __init__(self, Player):
        super(ChrOverView, self).__init__(layoutType='H')
        self.layout.addWidget(ChrStatsWidget(Player))
        #self.layout.addWidget(ChrInfo(Player))