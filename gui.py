from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QPushButton,
                             QVBoxLayout, QLabel)
from PyQt5.QtCore import Qt, QTimer
import quiz
class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz App")
        self.setGeometry(100, 100, 400, 300) # x, y , width, height
        self.questions = quiz.getQuiz()
        self.current_question = 0
        self.init_ui()
    def init_ui(self):
        # Create layout
        layout = QVBoxLayout()
        
        # Create and configure the question label
        self.question_label = QLabel("")
        self.question_label.setStyleSheet("font-size: 18px; padding: 10px;")
        self.question_label.setWordWrap(True)
        self.question_label.setAlignment(Qt.AlignCenter)
        self.skip = QPushButton("Skip question", self)
        
        self.skip.clicked.connect(lambda checked: self.load_next_question())
        # Add Label to the layout
        layout.addWidget(self.question_label)
        layout.addWidget(self.skip)
        # Layout containing the answers
        self.answers_group = []
        self.answers = QVBoxLayout()
        layout.addLayout(self.answers)
        
        self.load_question(0)
        self.setLayout(layout)


    def update_layout(self, question, answers, correct):
        self.question_label.setText(question)
        self.clear_answers()
        self.answers_group.clear()
        
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        
        if (len(answers) == 4):
            for i in range(2):
                btn = QPushButton(answers[i], self)
                btn.clicked.connect(lambda checked, text = answers[i], b= btn: self.check_answer(text, correct, b))
                self.answers_group.append(btn)
                row1.addWidget(btn)
            for i in range(2, 4):
                btn = QPushButton(answers[i], self)
                btn.clicked.connect(lambda checked, text = answers[i], b= btn: self.check_answer(text, correct, b))
                self.answers_group.append(btn)
                row2.addWidget(btn)
            
            self.answers.addLayout(row1)
            self.answers.addLayout(row2)
        else:
            for i in range(2):
                btn = QPushButton(answers[i], self)
                btn.clicked.connect(lambda checked, text = answers[i], b = btn: self.check_answer(text, correct, b))
                self.answers_group.append(btn)
                row1.addWidget(btn)
                
            self.answers.addLayout(row1)
    
    def load_end_screen(self):
        self.congratulation_label = QLabel("Congratulations, you finished the quiz! ")
        self.congratulation_label.setStyleSheet("font-size: 18px; padding: 10px;")
        self.congratulation_label.setAlignment(Qt.AlignCenter)
        
        self.clear_layout()
        self.layout().addWidget(self.congratulation_label)
        
    
    def clear_layout(self):
        if self.layout():
            self.clear_answers()
            while self.layout().count():
                item = self.layout().takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
                elif item.layout():
                    while item.layout().count():
                        child = item.layout().takeAt(0)
                        if child.layout():
                            child.widget().deleteLater()
            
        
         
    def check_answer(self, text, correct, b: QPushButton):
        for btn in self.answers_group:
            btn.setEnabled(False)
        if text == correct:
            b.setStyleSheet("border: 1px solid #00FF00; background-color: white; border-radius: 15px; color: #00FF00")
        else:
            b.setStyleSheet("border: 1px solid red; background-color: white; border-radius: 15px; color: red")
        
        QTimer.singleShot(2000, self.load_next_question)

    def load_question(self, index):
        if (index < len(self.questions)):
            q = self.questions[index]
            self.update_layout(q['question'], q['answers'], q['correct'])
        else:
            self.load_end_screen()

    def load_next_question(self):
        self.current_question += 1
        self.load_question(self.current_question)
    
    def clear_answers(self):
         while self.answers.count():
            child = self.answers.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                while child.layout().count():
                    subChild = child.layout().takeAt(0)
                    if subChild.widget():
                        subChild.widget().deleteLater()