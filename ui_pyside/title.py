'''
Created on Apr 3, 2019

@author: ajacobs
'''

from PySide2 import QtCore, QtGui, QtWidgets

class Banner(QtWidgets.QWidget):
    def __init__(self, Player):
        super(Banner, self).__init__()
        print ('end')
        self.Player = Player
        
        #Setting up widget paramaters
        self.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.setObjectName("bannerWidget")
        
        #Setting layout that frame uses
        self.bannerLayout = QtWidgets.QVBoxLayout(self)
        self.bannerLayout.setSpacing(1)
        self.bannerLayout.setContentsMargins(QtCore.QMargins(1,1,1,1))
        self.bannerLayout.setObjectName("VLayout")
        
        font = QtGui.QFont()
        
        playerFont = 20
        classFont = 10
        
        font.setPointSize(playerFont)
        print (Player.getName())
        self.playerLabel = QtWidgets.QLabel(str(Player.getName()))
        self.playerLabel.setFont(font)
        self.playerLabel.setObjectName('playerLabel')
        self.bannerLayout.addWidget(self.playerLabel)
        
        self.playerLevel = QtWidgets.QProgressBar()
        self.playerLevel.setMinimum(0)
        self.playerLevel.setMaximum(100)
        self.playerLevel.setValue(50)
        self.playerLevel.setObjectName('playerLevel')
        self.bannerLayout.addWidget(self.playerLevel)
        
        font.setPointSize(classFont)
        self.playerInfoLabel = QtWidgets.QLabel(self.buildPlayerInfoStr())
        self.playerInfoLabel.setFont(font)
        self.playerInfoLabel.setObjectName('playerInfo')
        self.bannerLayout.addWidget(self.playerInfoLabel)
        
        
        
    def buildPlayerInfoStr(self):
        playerInfo = self.Player.getRace()
        for cls, lvl in self.Player.getClass().items():
            playerInfo += r'/lvl %s %s' %(str(lvl), str(cls))
        return playerInfo
        