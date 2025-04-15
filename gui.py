from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QPushButton,
                             QVBoxLayout, QLabel)
from PyQt5.QtCore import Qt, QTimer
import quiz
class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz App")
        self.setGeometry(100, 100, 600, 500) # x, y , width, height
        self.questions = quiz.getQuiz()
        self.current_question = 0
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.load_front_screen()    
        

    def update_layout(self, question, answers, correct):
        self.question_label.setText(question)
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
    
    def create_question_layout(self):
        self.clear_layout()
        self.question_label = QLabel("")
        self.question_label.setStyleSheet("font-size: 18px; padding: 10px;")
        self.question_label.setWordWrap(True)
        self.question_label.setAlignment(Qt.AlignCenter)
        self.skip = QPushButton("Skip question", self)
        
        self.skip.clicked.connect(lambda checked: self.load_next_question())
        self.main_layout.addWidget(self.question_label)
        self.main_layout.addWidget(self.skip)
        
        self.answers_group = []
        self.answers = QVBoxLayout()
        self.main_layout.addLayout(self.answers)
        
        self.load_question(0)

    def load_front_screen(self):
        self.clear_layout()
        self.front_layout = QVBoxLayout()
        
        self.greeting_label = QLabel("Welcome to the quiz app!")
        self.greeting_label.setStyleSheet("font-size: 18px; padding: 10px;")
        self.greeting_label.setAlignment(Qt.AlignCenter)
        
        self.start_btn = QPushButton("Play")
        self.start_btn.clicked.connect(lambda checked, b = self.start_btn: self.create_question_layout())
        self.define_btn = QPushButton("Define")
        
        self.btn_row_layout = QHBoxLayout()
        self.btn_row_layout.addWidget(self.start_btn)
        self.btn_row_layout.addWidget(self.define_btn)
        
        self.front_layout.addWidget(self.greeting_label)
        self.front_layout.addLayout(self.btn_row_layout)
        
        self.main_layout.addWidget(self.greeting_label)
        self.main_layout.addLayout(self.front_layout)
        
    
    def load_end_screen(self):
        self.clear_layout()
        
        self.congratulation_label = QLabel("Congratulations, you finished the quiz! ")
        self.congratulation_label.setStyleSheet("font-size: 18px; padding: 10px;")
        self.congratulation_label.setAlignment(Qt.AlignCenter)
        
        self.main_layout.addWidget(self.congratulation_label)
        
    
    def clear_layout(self):
        if self.main_layout:
            while self.main_layout.count():
                item = self.main_layout.takeAt(0)
                if item.widget():
                    item.widget().deleteLater()
                elif item.layout():
                    # Clear the child layout recursively
                    while item.layout().count():
                        child = item.layout().takeAt(0)
                        if child.widget():
                            child.widget().deleteLater()
                        elif child.layout():
                            self.clear_child_layout(child.layout())
                    
    def clear_child_layout(self, layout):
        """Helper method to clear nested layouts"""
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_child_layout(item.layout())
            
    def check_answer(self, text, correct, b: QPushButton):
        for btn in self.answers_group:
            btn.setEnabled(False)
        if text == correct:
            b.setStyleSheet("border: 1px solid #00FF00; background-color: white; border-radius: 15px; color: #00FF00")
        else:
            b.setStyleSheet("border: 1px solid red; background-color: white; border-radius: 15px; color: red")
        
        QTimer.singleShot(2000, self.load_next_question)

    def load_question(self, index):
        self.clear_answers()
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