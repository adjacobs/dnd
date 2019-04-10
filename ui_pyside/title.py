'''
Created on Apr 3, 2019

@author: ajacobs
'''

from PySide2 import QtCore, QtGui, QtWidgets

class Title(QtWidgets.QWidget):
    def __init__(self, Player):
        super(Title, self).__init__()
        self.Player = Player
        
        #Setting up widget paramaters
        self.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.setObjectName("bannerWidget")
        
        #Setting layout that frame uses
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setSpacing(1)
        self.layout.setContentsMargins(QtCore.QMargins(1,1,1,1))
        self.layout.setObjectName("VLayout")
        
        #Setting font class
        font = QtGui.QFont()
        font.setWeight(50)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        
        #Setting class vairables (Font)
        playerFont = 20
        classFont = 10
        
        #Setting up player name label
        font.setPointSize(playerFont)
        self.playerLabel = QtWidgets.QLabel(str(self.Player.getName()))
        self.playerLabel.setFont(font)
        self.playerLabel.setObjectName('playerLabel')
        self.layout.addWidget(self.playerLabel)
        
        #Setting up player experience meter
        self.playerLevel = QtWidgets.QProgressBar()
        self.playerLevel.setMinimum(0)
        self.playerLevel.setMaximum(100)
        self.playerLevel.setValue(50)
        self.playerLevel.setObjectName('playerLevel')
        self.layout.addWidget(self.playerLevel)
        
        #Setting up player race and class label
        font.setPointSize(classFont)
        self.playerInfoLabel = QtWidgets.QLabel(self.buildPlayerInfoStr())
        self.playerInfoLabel.setFont(font)
        self.playerInfoLabel.setObjectName('playerInfo')
        self.layout.addWidget(self.playerInfoLabel)
        
        
    '''Function to go through the Player class and build out the string to be used
    for the player info label. Can handle multiple class and levels in thouse classes.'''  
    def buildPlayerInfoStr(self):
        playerInfo = self.Player.getRace()
        for cls, lvl in self.Player.getClass().items():
            playerInfo += r'/lvl %s %s' %(str(lvl), str(cls))
        return playerInfo
        