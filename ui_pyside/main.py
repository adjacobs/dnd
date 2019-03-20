
from PySide2 import QtCore, QtGui, QtWidgets

#Import of UI elemenets
from dnd.ui_pyside.stats import StatWidget
from dnd.ui_pyside.skills import SkillWidget

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
        self.centralGLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.centralGLayout.setObjectName("centralGLayout")
        
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
        self.addStats()
        self.addSkills()
        
    def retranslateUi(self):
        self.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "DnDWindow", None, -1))
        self.dropDownMenu.setTitle(QtWidgets.QApplication.translate("MainWindow", "dropDownMenu", None, 1))
        self.dropDownMenuItem.setText(QtWidgets.QApplication.translate("MainWindow", "dropDownMenuItem", None, -1))
        
    def addStats(self):
        '''Builds Frame for stat widgets to get added to and adds the frame to the central widget'''
        #Setting up frame pramaters
        self.statsFrame = QtWidgets.QFrame(self.centralwidget)
        self.statsFrame.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.statsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.statsFrame.setObjectName("statsFrame")
        
        #Adding frame to central layout
        self.centralGLayout.addWidget(self.statsFrame)
        
        #Setting frame layout for stat widgets to be added to
        self.statsFrameVLayout = QtWidgets.QVBoxLayout(self.statsFrame)
        self.statsFrameVLayout.setObjectName("statsFrameVLayout")
        
        for stat in self.Player.stats:
            self.statsFrameVLayout.addWidget(StatWidget(stat, self))
    
    def addSkills(self):
        '''Builds Frame for skills widgets to get added to and adds the frame to the central widget'''
        #Setting up frame pramaters
        self.skillsFrame = QtWidgets.QFrame(self.centralwidget)
        self.skillsFrame.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.skillsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.skillsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.skillsFrame.setObjectName("statsFrame")
        
        #Adding frame to central layout
        self.centralGLayout.addWidget(self.skillsFrame)
        
        #Setting frame layout for skills to be added to
        self.skillsFrameVLayout = QtWidgets.QVBoxLayout(self.skillsFrame)
        self.skillsFrameVLayout.setObjectName("statsFrameVLayout")
        
        skills=['Athletics (Str)', 'Acrobatics (Dex)', 'Poison (Con)','Arcana (Int)', 'Animal Handling (Wis)', 'Deception (Cha)']
        
        for s in skills:
            self.skillsFrameVLayout.addWidget(SkillWidget(s))
    
    def testFunction(self):
        print ('testFunction working')
