import requests
from pprint import pprint
from random import randint
base_url = "https://opentdb.com/api.php?amount=10&type=boolean"
amount = 10
res = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

data = res.json()

questions = [
            {
                "question": "What is the capital of France?",
                "answers": ["Berlin", "Madrid", "Paris", "Rome"],
                "correct": "Paris"
            },
            {
                "question": "Which language is used for web apps?",
                "answers": ["Python", "HTML", "C++", "Java"],
                "correct": "HTML"
            },
            {
                "question": "What’s the result of 3 * 3?",
                "answers": ["6", "9", "12", "3"],
                "correct": "9"
            }
]

def getQuiz():
    return questions