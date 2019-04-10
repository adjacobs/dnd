'''
Created on Apr 4, 2019

@author: ajacobs
'''
from dnd.ui_pyside.traits import Traits
from dnd.ui_pyside.title import Title
from dnd.ui_pyside.util import FrameWidget

class Banner(FrameWidget):
    def __init__(self, Player):
        super(Banner, self).__init__(layoutType='H')
        self.Player = Player
        self.layout.addWidget(Title(self.Player))
        self.layout.addWidget(Traits(self.Player))
