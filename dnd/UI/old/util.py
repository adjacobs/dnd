'''
Created on Mar 8, 2019

@author: ajacobs
'''

from PySide2 import QtWidgets


class SectionLayout(QtWidgets.QVBoxLayout):
    def __init__(self):
        super(SectionLayout, self).__init__()
        self.setSpacing(0)

'''Framed wiget to be called by all sections. Allowing for universal changes to framed out sections'''   
class SectionFrame(QtWidgets.QFrame): 
    def __init__(self):
        super(SectionFrame, self).__init__()
        self.layout=SectionLayout()
        self.setLineWidth(1)
        self.setFrameStyle(QtWidgets.QFrame.Box|QtWidgets.QFrame.Sunken)  
        self.setLayout(self.layout)  
