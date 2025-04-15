import requests
from pprint import pprint
from random import randint
import html

base_url = "https://opentdb.com/api.php?amount=10"
amount = 10
res = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean")
"""https://opentdb.com/api.php?amount=10&difficulty=easy&type=multiple"""

difficulty = ["easy", "difficult", "medium"]
type = ["multiple", "boolean"]

data = res.json()

def format_data(data):
    clean_data = []
    for question in data:
        q = {}
        q['question'] = question['question']
        q['correct'] = question['correct_answer']
        q['difficulty'] = question['difficulty']
        q['answers'] = [question['correct_answer']]
        for answer in question['incorrect_answers']:
            q['answers'].append(answer)

        clean_data.append(q)
        
    return clean_data
#pprint(format_data(data['results']))

def getQuiz():
    return format_data(data['results'])