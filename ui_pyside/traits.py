'''
Created on Apr 4, 2019

@author: ajacobs
'''
from dnd.ui_pyside.util import *

class Traits(FrameWidget):
    def __init__(self, Player):
        super(Traits, self).__init__(layoutType='V')
        self.Player = Player
        
        self.layout.setSpacing(2)
        
        self.combatWidget = Widget(layoutType = 'H')
        self.passiveWidget = Widget(layoutType = 'H')
        
        self.layout.addWidget(self.combatWidget)
        self.layout.addWidget(self.passiveWidget)
        
        self.combatWidget.layout.addWidget(InputWidgetV('Proficiency'))
        self.combatWidget.layout.addWidget(InputWidgetV('AC'))
        self.combatWidget.layout.addWidget(InputWidgetV('Initiative'))
        self.combatWidget.layout.addWidget(InputWidgetV('Speed'))
        self.combatWidget.layout.addWidget(InputWidgetV('Insperation'))
        
        self.passiveWidget.layout.addWidget(InputWidgetH('Passive Insight'))
        self.passiveWidget.layout.addWidget(InputWidgetH('Passive Investigation'))
        self.passiveWidget.layout.addWidget(InputWidgetH('Passive Insperation'))