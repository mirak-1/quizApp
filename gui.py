from PyQt5.QtWidgets import (QApplication, QWidget, QRadioButton, QHBoxLayout, QPushButton,
                             QVBoxLayout, QLabel, QButtonGroup)
from PyQt5.QtCore import Qt
class QuizApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz App")
        self.setGeometry(100, 100, 400, 300) # x, y , width, height
        self.init_ui()
    
    def init_ui(self):
        # Create layout
        layout = QVBoxLayout()
        
        # Create and configure the question label
        self.question_label = QLabel("")
        self.question_label.setStyleSheet("font-size: 18px; padding: 10px;")
        self.question_label.setWordWrap(True)
        self.question_label.setAlignment(Qt.AlignCenter)
        
        # Add Label to the layout
        layout.addWidget(self.question_label)
        
        # Layout containing the answers
        self.answers_group = []
        self.answers = QVBoxLayout()
        layout.addLayout(self.answers)
        
        self.setLayout(layout)


    def update_layout(self, question, answers, correct):
        self.question_label.setText(question)
        
        while self.answers.count():
            child = self.answers.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                while child.layout().count():
                    subChild = child.layout().takeAt(0)
                    if subChild.widget():
                        subChild.widget().deleteLater()
        
        self.answers_group.clear()
        
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        
        if (len(answers) == 4):
            for i in range(2):
                btn = QPushButton(answers[i], self)
                btn.clicked.connect(lambda checked, text = answers[i]: self.check_answer(text, correct))
                self.answers_group.append(btn)
                row1.addWidget(btn)
            for i in range(2, 4):
                btn = QPushButton(answers[i], self)
                btn.clicked.connect(lambda checked, text = answers[i]: self.check_answer(text, correct))
                self.answers_group.append(btn)
                row2.addWidget(btn)
            
            self.answers.addLayout(row1)
            self.answers.addLayout(row2)
        else:
            for i in range(2):
                btn = QPushButton(answers[i], self)
                btn.clicked.connect(lambda checked, text = answers[i]: self.check_answer(text, correct))
                self.answers_group.append(btn)
                row1.addWidget(btn)
                
            self.answers.addLayout(row1)
            
    def check_answer(self, text, correct):
        if text == correct:
            print("Correct answer! ")
        else:
            print("Wrong answer! ")
    