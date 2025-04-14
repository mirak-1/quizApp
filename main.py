import sys
from gui import QuizApp
import quiz
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint

app = QApplication(sys.argv)
window = QuizApp()
data = quiz.getQuiz()

window.show()
sys.exit(app.exec_())