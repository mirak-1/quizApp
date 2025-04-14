import requests
from pprint import pprint

base_url = "https://opentdb.com/api.php?amount=10&type=boolean"
amount = 10
res = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

#res = requests.get("https://opentdb.com/api_category.php")
data = res.json()
#categoriesJSON = data['trivia_categories']
#pprint(categoriesJSON)

# iterate throug the items
#for element in categoriesJSON:
#    print(f"id {element['id']}, name: {element['name']}")

#pprint(data['results'])

def getQuiz():
    return data['results']