"""
Created on Apr 3, 2019

@author: ajacobs
"""

from PySide2 import QtCore, QtGui, QtWidgets


class Title(QtWidgets.QWidget):
    def __init__(self, player):
        super(Title, self).__init__()
        self.player = player
        
        # Setting up widget parameters
        self.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.setObjectName("bannerWidget")
        
        # Setting layout that frame uses
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setSpacing(1)
        self.layout.setContentsMargins(QtCore.QMargins(1, 1, 1, 1))
        self.layout.setObjectName("VLayout")
        
        # Setting font class
        font = QtGui.QFont()
        font.setWeight(50)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        
        # Setting class vairables (Font)
        player_font = 20
        class_font = 10
        
        # Setting up player name label
        font.setPointSize(player_font)
        player_label = QtWidgets.QLabel(str(self.player.name))
        player_label.setFont(font)
        player_label.setObjectName('playerLabel')
        self.layout.addWidget(player_label)
        
        # Setting up player experience meter
        self.player_level = QtWidgets.QProgressBar()
        self.player_level.setMinimum(0)
        self.player_level.setMaximum(100)
        self.player_level.setValue(50)
        self.player_level.setObjectName('playerLevel')
        self.layout.addWidget(self.player_level)
        
        # Setting up player race and class label
        font.setPointSize(class_font)
        player_info_label = QtWidgets.QLabel('test player label')
        player_info_label.setFont(font)
        player_info_label.setObjectName('playerInfo')
        self.layout.addWidget(player_info_label)

    def build_player_info_str(self):
        """Function to go through the Player class and build out the string to be used
        for the player info label. Can handle multiple class and levels in thouse classes."""
        player_info = self.Player.getRace()
        for cls, lvl in self.Player.getClass().items():
            player_info += r'/lvl %s %s' %(str(lvl), str(cls))
        return player_info
