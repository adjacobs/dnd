""""
Created on Mar 21, 2019

@author: ajacobs
"""
from PySide2 import QtCore, QtGui, QtWidgets


class DetailsWidget(QtWidgets.QFrame):
    def __init__(self):
        super(DetailsWidget, self).__init__()
        
        '''Builds Frame for stat widgets to get added to and adds the frame to the central widget'''
        # Setting up frame parameter
        self.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setObjectName("specsFrame")
        
        # self.setMaximumWidth(100)
        
        # Setting frame layout for stat widgets to be added to
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setObjectName("specsLayout")
        
        self.layout.addWidget(CombatFrame())
        self.layout.addWidget(HealthFrame())


class CombatFrame(QtWidgets.QFrame):
    def __init__(self):
        super(CombatFrame, self).__init__()
        
        '''Builds Frame for stat widgets to get added to and adds the frame to the central widget'''
        # Setting up frame parameter
        self.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setObjectName("combatFrame")
        
        # self.setMaximumWidth(100)
        
        # Setting frame layout for stat widgets to be added to
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setObjectName("combatLayout")
        
        self.min_size = QtCore.QSize(50, 50)
        self.max_size = QtCore.QSize(50, 50)
        self.alignment = QtCore.Qt.AlignCenter
        
        self.font = QtGui.QFont()
        self.font.setWeight(50)
        self.font.setUnderline(False)
        self.font.setStrikeOut(False)
        self.font.setBold(False)
        
        self.buildACFrame()
        self.build_speed_frame()
        self.buildInitiativeFrame()
        
    def build_ac_fame(self):
        ac_frame = QtWidgets.QFrame()
        ac_frame.setFrameShape(QtWidgets.QFrame.Panel)
        ac_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        ac_frame.setObjectName("acFrame")
        
        ac_layout = QtWidgets.QVBoxLayout(ac_frame)
        ac_layout.setObjectName('acLayout')

        ac_line_edit = QtWidgets.QLineEdit()
        ac_line_edit.setMinimumSize(self.min_size)
        ac_line_edit.setMaximumSize(self.max_size)
        ac_line_edit.setFont(self.font)
        ac_line_edit.setAlignment(self.alignment)
        
        ac_label = QtWidgets.QLabel('Armor Class')
        
        ac_layout.addWidget(ac_line_edit)
        ac_layout.addWidget(ac_label)
        
        self.layout.addWidget(ac_frame)
        
    def build_speed_frame(self):
        speed_frame = QtWidgets.QFrame()
        speed_frame.setFrameShape(QtWidgets.QFrame.Panel)
        speed_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        speed_frame.setObjectName("speedFrame")
        
        speed_layout = QtWidgets.QVBoxLayout(speed_frame)
        speed_layout.setObjectName('speedLayout')
        
        speed_line_edit = QtWidgets.QLineEdit()
        speed_line_edit.setMinimumSize(self.min_size)
        speed_line_edit.setMaximumSize(self.max_size)
        speed_line_edit.setFont(self.font)
        speed_line_edit.setAlignment(self.alignment)
        
        speed_label = QtWidgets.QLabel('Speed')
        
        speed_layout.addWidget(speed_line_edit)
        speed_layout.addWidget(speed_label)
        
        self.layout.addWidget(speed_frame)
        
    def buildInitiativeFrame(self):
        initiative_frame = QtWidgets.QFrame()
        initiative_frame.setFrameShape(QtWidgets.QFrame.Panel)
        initiative_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        initiative_frame.setObjectName("initiativeFrame")
        
        initiative_layout = QtWidgets.QVBoxLayout(initiative_frame)
        initiative_layout.setObjectName('initiativeLayout')
        
        initiative_line_edit = QtWidgets.QLineEdit()
        initiative_line_edit.setMinimumSize(self.min_size)
        initiative_line_edit.setMaximumSize(self.max_size)
        initiative_line_edit.setFont(self.font)
        initiative_line_edit.setAlignment(self.alignment)
        
        initiative_label = QtWidgets.QLabel('Initiative')
        
        initiative_layout.addWidget(initiative_line_edit)
        initiative_layout.addWidget(initiative_label)
        
        self.layout.addWidget(initiative_frame)


class HealthFrame(QtWidgets.QFrame):
    def __init__(self):
        super(HealthFrame, self).__init__()
        
        '''Builds Frame for stat widgets to get added to and adds the frame to the central widget'''
        # Setting up frame pramaters
        self.setGeometry(QtCore.QRect(260, 50, 184, 641))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Plain)
        self.setObjectName("healthFrame")
        
        # self.setMaximumWidth(100)
        
        # Setting frame layout for stat widgets to be added to
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setObjectName("combatSpecsLayout")
        
        self.min_size = QtCore.QSize(50, 50)
        self.max_size = QtCore.QSize(50, 50)
        self.alignment = QtCore.Qt.AlignCenter
        
        self.font = QtGui.QFont()
        self.font.setWeight(50)
        self.font.setUnderline(False)
        self.font.setStrikeOut(False)
        self.font.setBold(False)
        
        self.build_health_frame()
        self.build_temp_health_frame()
        
    def build_health_frame(self):
        health_frame = QtWidgets.QFrame()
        health_frame.setFrameShape(QtWidgets.QFrame.Panel)
        health_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        health_frame.setObjectName("healthFrame")
        
        health_layout = QtWidgets.QHBoxLayout(health_frame)
        health_layout.setObjectName('healthLayout')
        
        minus_health_button = QtWidgets.QPushButton("-")
        
        health_line_edit = QtWidgets.QLineEdit()
        health_line_edit.setMinimumSize(QtCore.QSize(50, 50))
        health_line_edit.setMaximumSize(QtCore.QSize(50, 50))
        health_line_edit.setFont(self.font)
        health_line_edit.setMaxLength(2)
        health_line_edit.setAlignment(self.alignment)
        
        add_health_button = QtWidgets.QPushButton("+")
        
        health_layout.addWidget(minus_health_button)
        health_layout.addWidget(health_line_edit)
        health_layout.addWidget(add_health_button)
        
        self.layout.addWidget(health_frame)
    
    def build_temp_health_frame(self):
        temp_health_frame = QtWidgets.QFrame()
        temp_health_frame.setFrameShape(QtWidgets.QFrame.Panel)
        temp_health_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        temp_health_frame.setObjectName("tempHealthFrame")
        
        temp_health_layout = QtWidgets.QHBoxLayout(temp_health_frame)
        temp_health_layout.setObjectName('tempHealthLayout')
        
        minus_temp_health_button = QtWidgets.QPushButton("-")
        
        temp_health_line_edit = QtWidgets.QLineEdit()
        temp_health_line_edit.setMinimumSize(QtCore.QSize(50, 50))
        temp_health_line_edit.setMaximumSize(QtCore.QSize(50, 50))
        temp_health_line_edit.setFont(self.font)
        temp_health_line_edit.setMaxLength(2)
        temp_health_line_edit.setAlignment(self.alignment)
        
        add_temp_health_button = QtWidgets.QPushButton("+")
        
        temp_health_layout.addWidget(minus_temp_health_button)
        temp_health_layout.addWidget(temp_health_line_edit)
        temp_health_layout.addWidget(add_temp_health_button)
        
        self.layout.addWidget(temp_health_frame)
