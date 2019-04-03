'''
Created on Apr 3, 2019

@author: ajacobs
'''
import sys 
from dnd.engine.player import Player
from PySide2 import QtCore, QtGui, QtWidgets

from dnd.ui_pyside.title import Banner
from dnd.ui_pyside.statsV2 import StatsWidget


class UI(Banner):
    def __init__(self):
        super(UI, self).__init__(Player())


app = QtWidgets.QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec_())