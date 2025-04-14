import sys
from gui import QuizApp
import quiz
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint

app = QApplication(sys.argv)
window = QuizApp()
data = quiz.getQuiz()

qstObject = data[randint(0, len(data))]

question = qstObject['question']
answers = ['True', 'False']
correct = qstObject['correct_answer']

window.update_layout(question, answers, correct)
window.show()
sys.exit(app.exec_())