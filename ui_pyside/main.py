

from PySide2 import QtCore, QtWidgets

# Import of UI elements
from ui_pyside.stats import ChrStatsWidget
from ui_pyside.traits import Traits
from ui_pyside.title import Title
from ui_pyside.util import FrameWidget


class UI(QtWidgets.QMainWindow):
    def __init__(self, player_engine):
        super(UI, self).__init__()
        
        # Setting playerEnding to class variable
        self.player = player_engine()
        
        self.setObjectName("MainWindow")
        self.resize(836, 1051)

        # Set up central widget for the main window that allows other widgets to be added to.
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.setCentralWidget(self.central_widget)
        
        # Sets up central widget layout for central widget that all UI elements will be added to
        self.central_v_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.central_v_layout.setObjectName("centralGLayout")
    
        # Set up menu par parameters
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 836, 21))
        self.menu_bar.setObjectName("menu_bar")
        
        # Set up drop down menu
        self.drop_down_menu = QtWidgets.QMenu(self.menu_bar)
        self.drop_down_menu.setObjectName('drop_down_menu')
        
        # Add menu bar to Main Window
        self.setMenuBar(self.menu_bar)
        
        # Build drop down item and connect to function
        self.drop_down_menu_item = QtWidgets.QAction(self)
        self.drop_down_menu_item.setObjectName("drop_down_menu_item")
        # self.drop_down_menu_item.triggered.connect(self.player.test_unction)
        
        # Adds drop down menu to menu
        self.drop_down_menu.addAction(self.drop_down_menu_item)
        self.menu_bar.addAction(self.drop_down_menu.menuAction())
        
        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

        # Adding UI elements
        self.central_v_layout.addWidget(Banner(self.player))
        self.central_v_layout.addWidget(ChrOverView(self.player))
        
    def translate_ui(self):
        self.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "DnDWindow", None, -1))
        self.drop_down_menu.setTitle(QtWidgets.QApplication.translate("MainWindow", "dropDownMenu", None, 1))
        self.drop_down_menu_item.setText(QtWidgets.QApplication.translate("MainWindow", "dropDownMenuItem", None, -1))
    
    def refresh_skills(self):
        """Goes through skill widgets and makes sure that the visual matches what the Player class has."""
        for skill in self.skillsFrame.findChildren(QtWidgets.QFrame, 'skillFrame'):
            skill.setModifier()


class Banner(FrameWidget):
    def __init__(self, player):
        super(Banner, self).__init__(layout_type='H')
        self.layout.addWidget(Title(player))
        self.layout.addWidget(Traits(player))


class ChrOverView(FrameWidget):
    def __init__(self, player):
        super(ChrOverView, self).__init__(layout_type='H')
        self.layout.addWidget(ChrStatsWidget(player))
        # self.layout.addWidget(ChrInfo(Player))
