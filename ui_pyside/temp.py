
'''

Created on Apr 3, 2019

@author: ajacobs
'''

from PySide2 import QtCore, QtGui, QtWidgets


class Frame(QtWidgets.QFrame):
    def __init__(self):
        super(Frame, self).__init__()    
        print ('cat')

this=Frame()