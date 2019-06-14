'''
Created on Apr 4, 2019

@author: ajacobs
'''
from dnd.ui_pyside.util import *


class Traits(FrameWidget):
    def __init__(self, Player):
        super(Traits, self).__init__(layout_type='V')
        self.Player = Player
        
        self.layout.setSpacing(2)
        
        self.combat_widget = Widget(layout_type='H')
        self.passiveWidget = Widget(layout_type='H')

        self.layout.addWidget(self.combat_widget)
        self.layout.addWidget(self.passiveWidget)
        
        self.combat_widget.layout.addWidget(InputWidgetV('Proficiency'))
        self.combat_widget.layout.addWidget(InputWidgetV('AC'))
        self.combat_widget.layout.addWidget(InputWidgetV('Initiative'))
        self.combat_widget.layout.addWidget(InputWidgetV('Speed'))
        self.combat_widget.layout.addWidget(InputWidgetV('Inspiration'))
        
        self.passiveWidget.layout.addWidget(InputWidgetH('Passive Insight'))
        self.passiveWidget.layout.addWidget(InputWidgetH('Passive Investigation'))
        self.passiveWidget.layout.addWidget(InputWidgetH('Passive Inspiration'))
