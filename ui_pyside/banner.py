""""
Created on Apr 4, 2019

@author: ajacobs
"""
from ui_pyside.traits import Traits
from ui_pyside.title import Title
from ui_pyside.util import FrameWidget


class Banner(FrameWidget):
    def __init__(self, player):
        super(Banner, self).__init__(layoutType='H')
        self.player = player
        self.layout.addWidget(Title(self.player))
        self.layout.addWidget(Traits(self.player))
