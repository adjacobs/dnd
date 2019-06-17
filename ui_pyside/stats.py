"""
Created on Mar 28, 2019

@author: ajacobs
"""
from PySide2 import QtCore, QtGui, QtWidgets


class ChrStatsWidget(QtWidgets.QFrame):
    def __init__(self, player):
        super(ChrStatsWidget, self).__init__()
        """Builds Frame for stat widgets to get added to and adds the frame to the central widget"""
        # Setting up frame parameters
        self.setGeometry(QtCore.QRect(260, 100, 184, 641))
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("statsFrame")
        
        self.setMaximumWidth(200)
        
        # Setting frame layout for stat widgets to be added to
        stats_frame_v_layout = QtWidgets.QVBoxLayout(self)
        stats_frame_v_layout.setSpacing(2)
        stats_frame_v_layout.setContentsMargins(1, 1, 1, 1)
        stats_frame_v_layout.setObjectName("statsFrameVLayout")
        
        # Go through the player stats and build out a frame widget for each
        # Passing in "self" so stat widgets can all refresh together
        skills = player.get_skills(byStat=True)
        for stat in player.get_stats():
            stats_frame_v_layout.addWidget(StatWidget(stat, skills[stat.name]))


class StatWidget(QtWidgets.QFrame):
    def __init__(self, stat, skills):
        super(StatWidget, self).__init__()
        self.stat = stat
        self.skills = []

        # Setting parameter for QFrame inherited class
        self.setGeometry(QtCore.QRect(50, 50, 50, 50))
        self.setFrameShape(QtWidgets.QFrame.Panel)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setObjectName("mainFrame")
        
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.main_layout.setContentsMargins(2, 2, 2, 2)
        self.main_layout.setSpacing(1)
        self.main_layout.setObjectName("mainVLayout")
        
        # Set font class for UI
        # Set shared font paramaters
        self.font = QtGui.QFont()
        self.font.setWeight(50)
        self.font.setUnderline(False)
        self.font.setStrikeOut(False)
        self.font.setBold(False)
        
        self._build_stat_frame()
        self._build_save_frame()
        
        for skill in skills:
            widget = SkillWidget(skill)
            self.main_layout.addWidget(widget)
            self.skills.append(widget)
    
    def _build_stat_frame(self):
        # Set variables for size adjustment
        value_font = 10
        mod_font = 18
        stat_size = QtCore.QSize(20, 20)
        mod_size = QtCore.QSize(30, 30)
        layout_margin = QtCore.QMargins(2, 1, 1, 1)
        
        # Set up frame for stat
        stat_frame = QtWidgets.QFrame()
        stat_frame.setFrameShape(QtWidgets.QFrame.Panel)
        stat_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        stat_frame.setObjectName("statFrame")
        self.main_layout.addWidget(stat_frame)
        
        # Setting layout that frame uses
        stat_frame_v_layout = QtWidgets.QHBoxLayout(stat_frame)
        stat_frame_v_layout.setObjectName("statFrameVLayout")
        stat_frame_v_layout.setContentsMargins(layout_margin)
        
        # Set up label including adding to layout
        stat_label = QtWidgets.QLabel(self)
        stat_label.setText(self.stat.name)
        stat_label.setFont(self.font)
        stat_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        stat_label.setAlignment(QtCore.Qt.AlignCenter)
        stat_label.setObjectName("statLabel")
        stat_frame_v_layout.addWidget(stat_label)
        
        # Spacers set up (Used for both value and modifier)
        left_spacer_item = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        # Setting up value line edit. Including layout and adding to the frame
        self.font.setPointSize(value_font)
        value_h_layout = QtWidgets.QHBoxLayout()
        value_h_layout.setObjectName("valueHLayout")
        value_h_layout.addItem(left_spacer_item)
        self.value_line_edit = QtWidgets.QLineEdit(self)
        self.value_line_edit.setMinimumSize(stat_size)
        self.value_line_edit.setMaximumSize(stat_size)
        self.value_line_edit.setFont(self.font)
        self.value_line_edit.setMaxLength(2)
        self.value_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.value_line_edit.setObjectName("valueLineEdit")
        
        # Set value line edit validator
        only_int = QtGui.QIntValidator(0, 40)
        self.value_line_edit.setValidator(only_int)
        
        # Set value line edit value
        self.value_line_edit.setText(str(self.stat.value))
        value_h_layout.addWidget(self.value_line_edit)
        stat_frame_v_layout.addLayout(value_h_layout)
        
        # Setting up modifier line edit. Including layout and adding to the frame
        self.font.setPointSize(mod_font)
        mod_h_layout = QtWidgets.QHBoxLayout()
        mod_h_layout.setObjectName("modHLayout")
        mod_h_layout.addItem(left_spacer_item)
        self.mod_line_edit = QtWidgets.QLineEdit(self)
        self.mod_line_edit.setFont(self.font)
        self.mod_line_edit.setMaxLength(2)
        self.mod_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.mod_line_edit.setMinimumSize(mod_size)
        self.mod_line_edit.setMaximumSize(mod_size)
        self.mod_line_edit.setObjectName("modLineEdit")
        self.mod_line_edit.setReadOnly(True)
        
        # Set mod line edit value
        self.mod_line_edit.setText(str(self.stat.get_modifier()))
        mod_h_layout.addWidget(self.mod_line_edit)
        stat_frame_v_layout.addLayout(mod_h_layout)
        
        # Connect value line edit function
        self.value_line_edit.editingFinished.connect(self.set_value)
    
    def _build_save_frame(self):
        # Set variables for size adjustment
        prof_size = QtCore.QSize(10, 10)
        mod_size = QtCore.QSize(20, 20)
        layout_margin = QtCore.QMargins(5, 0, 15, 0)
        self.font.setPointSize(10)
        
        # Set up frame for stat
        save_frame = QtWidgets.QFrame()
        save_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        save_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        save_frame.setObjectName("saveFrame")
        self.main_layout.addWidget(save_frame)
        
        # Setting layout that frame uses
        save_frame_h_layout = QtWidgets.QHBoxLayout(save_frame)
        save_frame_h_layout.setObjectName("saveFrameVLayout")
        save_frame_h_layout.setContentsMargins(layout_margin)
        
        # Set prof/expert line edit including adding to layout
        self.prof_line_edit = QtWidgets.QLineEdit(self)
        self.prof_line_edit.setFont(self.font)
        self.prof_line_edit.setMaxLength(2)
        self.prof_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.prof_line_edit.setMinimumSize(prof_size)
        self.prof_line_edit.setMaximumSize(prof_size)
        self.prof_line_edit.setObjectName("saveProfLineEdit")
        self.prof_line_edit.setReadOnly(True)
        save_frame_h_layout.addWidget(self.prof_line_edit)
        
        # Set up spacer to offset the expertise line edit from the skills class.
        # This way everything lines up
        spacer = QtWidgets.QSpacerItem(prof_size.height(), prof_size.width())
        save_frame_h_layout.addSpacerItem(spacer)
        
        # Set up label including adding to layout
        label = QtWidgets.QLabel(self)
        label.setText('Save')
        label.setLayoutDirection(QtCore.Qt.LeftToRight)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setObjectName("label")
        save_frame_h_layout.addWidget(label)
        
        # Set up modifier line edit including adding to layout
        self.save_mod_line_edit = QtWidgets.QLineEdit(self)
        self.save_mod_line_edit.setFont(self.font)
        self.save_mod_line_edit.setMaxLength(2)
        self.save_mod_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.save_mod_line_edit.setMinimumSize(mod_size)
        self.save_mod_line_edit.setMaximumSize(mod_size)
        self.save_mod_line_edit.setObjectName("modLineEdit")
        self.save_mod_line_edit.setReadOnly(True)
        save_frame_h_layout.addWidget(self.save_mod_line_edit)
    
    def set_value(self):
        """Function to set value of stat as well as change modifier accordingly
        Can be set on the UI level"""
        input_value = self.value_line_edit.text()
        if input_value != str(self.stat.value):
            self.stat.set(input_value)
            self.mod_line_edit.setText(str(self.stat.get_modifier()))
            for skill in self.skills:
                skill.update_mod()
    
    def refresh_ui(self):
        """refresh function that checks that stat widget number matches
        the corresponding stat in the player class."""
        self.value_line_edit.setText(str(self.stat.value))
        self.mod_line_edit.setText(str(self.stat.get_modifier()))


class SkillWidget(QtWidgets.QFrame):
    def __init__(self, skill):
        super(SkillWidget, self).__init__()
        self.skill = skill
        
        # Set shared font parameters
        font = QtGui.QFont()
        font.setWeight(50)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setBold(False)
        
        # Set variables for size adjustment
        font.setPointSize(10)
        prof_size = QtCore.QSize(10, 10)
        mod_size = QtCore.QSize(20, 20)
        layout_margin = QtCore.QMargins(5,0,15,0)
        
        # Set up frame for stat
        self.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.setFrameShadow(QtWidgets.QFrame.Raised)
        self.setObjectName("skillFrame")
        
        # Setting layout that frame uses
        skill_frame_h_layout = QtWidgets.QHBoxLayout(self)
        skill_frame_h_layout.setObjectName("skillFrameVLayout")
        skill_frame_h_layout.setContentsMargins(layout_margin)
        
        # Set prof line edit including adding to layout
        self.prof_line_edit = QtWidgets.QLineEdit()
        self.prof_line_edit.setFont(font)
        self.prof_line_edit.setMaxLength(2)
        self.prof_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.prof_line_edit.setMinimumSize(prof_size)
        self.prof_line_edit.setMaximumSize(prof_size)
        self.prof_line_edit.setObjectName("profLineEdit")
        self.prof_line_edit.setReadOnly(True)
        skill_frame_h_layout.addWidget(self.prof_line_edit)
        
        # Set expertise line edit including adding to layout
        self.expertLineEdit = QtWidgets.QLineEdit()
        self.expertLineEdit.setFont(font)
        self.expertLineEdit.setMaxLength(2)
        self.expertLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.expertLineEdit.setMinimumSize(prof_size)
        self.expertLineEdit.setMaximumSize(prof_size)
        self.expertLineEdit.setObjectName("expertLineEdit")
        self.expertLineEdit.setReadOnly(True)
        skill_frame_h_layout.addWidget(self.expertLineEdit)
        
        # Set up label including adding to layout
        skill_label = QtWidgets.QLabel()
        skill_label.setText(skill.name)
        skill_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        skill_label.setAlignment(QtCore.Qt.AlignCenter)
        skill_label.setObjectName("skill_label")
        skill_frame_h_layout.addWidget(skill_label)
        
        # Set up modifier line edit including adding to layout
        self.mod_line_edit = QtWidgets.QLineEdit()
        self.mod_line_edit.setFont(font)
        self.mod_line_edit.setMaxLength(2)
        self.mod_line_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.mod_line_edit.setMinimumSize(mod_size)
        self.mod_line_edit.setMaximumSize(mod_size)
        self.mod_line_edit.setObjectName("modLineEdit")
        self.mod_line_edit.setReadOnly(True)
        skill_frame_h_layout.addWidget(self.mod_line_edit)
        
        self.update_mod()
    
    def update_mod(self):
        self.mod_line_edit.setText(str(self.skill.get_modifier(3)))
