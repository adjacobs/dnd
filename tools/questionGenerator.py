
from PySide2 import QtCore, QtGui, QtWidgets
import random

# Only needed for access to command line arguments
import sys
import os
os.environ['QT_MAC_WANTS_LAYER'] = '1'


class Questions:
    def __init__(self):
        self.questions = ['Question 1',
                          'Question 2',
                          'Question 3',
                          'Question 4',
                          'Question 5',
                          'Question 6']
        self.question_count = 2
        self.answered_questions = []

    def next_question(self):
        """
        Check that count is not at 0 then return question
        @return: String
        """
        if self.question_count:
            question_index = random.randint(0, len(self.questions)-1)
            question = self.questions[question_index]
            self.questions.pop(question_index)
            self.question_count += -1
            return question
        else:
            return ''


class QuestionsUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(QuestionsUI, self).__init__()
        self.questions = Questions()

        self.setObjectName("MainWindow")
        self.resize(500, 200)

        # Set up central widget for the main window that allows other widgets to be added to.
        self.central_widget = QtWidgets.QWidget(self)
        self.central_widget.setObjectName("central_widget")
        self.setCentralWidget(self.central_widget)

        # Sets up central widget layout for central widget that all UI elements will be added to
        self.central_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.central_layout.setObjectName("centralGLayout")
        self.central_layout.setAlignment(QtGui.Qt.AlignCenter)

        # Set question title
        self.question_font = QtGui.QFont()
        self.question_font.setWeight(20)
        self.question_font.setPointSize(30)

        self.question_label = QtWidgets.QLabel('Watch around the eyes!!!')
        self.question_label.setFont(self.question_font)
        self.central_layout.addWidget(self.question_label)

        # Change question
        self.next_question_btn = QtWidgets.QPushButton('Ready')
        self.next_question_btn.clicked.connect(self.next_question)
        self.central_layout.addWidget(self.next_question_btn)

        # Set up menu par parameters
        self.menu_bar = QtWidgets.QMenuBar(self)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 836, 21))
        self.menu_bar.setObjectName("menu_bar")

        # Set up drop down menu
        self.drop_down_menu = QtWidgets.QMenu(self.menu_bar)
        self.drop_down_menu.setObjectName('drop_down_menu')

        # Add menu bar to Main Window
        self.setMenuBar(self.menu_bar)

        # Build drop down item and connect to function
        self.drop_down_menu_item = QtWidgets.QAction(self)
        self.drop_down_menu_item.setObjectName("drop_down_menu_item")

        # Adds drop down menu to menu
        self.drop_down_menu.addAction(self.drop_down_menu_item)
        self.menu_bar.addAction(self.drop_down_menu.menuAction())

        self.translate_ui()
        QtCore.QMetaObject.connectSlotsByName(self)

    def translate_ui(self):
        self.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Questions", None, -1))
        self.drop_down_menu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Category", None, 1))
        self.drop_down_menu_item.setText(QtWidgets.QApplication.translate("MainWindow", "Menu Item", None, -1))

    def next_question(self):
        if self.next_question_btn.text() == 'Done':
            self.quit_app()

        question = self.questions.next_question()
        if question:
            self.question_label.setText(question)
            if self.next_question_btn.text() == 'Ready':
                self.next_question_btn.setText('Next Question')
        else:
            self.question_label.setText('All Questions Answered!!!!!')
            self.next_question_btn.setText('Done')

    @staticmethod
    def quit_app():
        # some actions to perform before actually quitting:
        app.exit()

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QtWidgets.QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QuestionsUI()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec_()