# Sprint 2 S2.6 - Assignment 9: Microservice Implementation (Milestone #2) Tester
# Christian McKinnon and Baorong Luo (tester.py)
# CS361, 2/24/2024
# This is a tester file that demonstrates 1.) Getting a random recipe,
# 2.) Tests adding a new recipe (something random), and 3.) Test matching a
# recipe based on a user's diet.

import requests # Once again, import the Python requests library for HTTP requests

# Flask URL for the recipe Microservice
# (Ensure that microservice.py is running before attempting this test!)
FLASK_URL = 'http://127.0.0.1:5000'

# Here we test getting a random recipe from data.json (Prompt 2):
def random_recipe_tester():
    response = requests.get(f'{FLASK_URL}/random_recipe')
    if response.status_code == 200:
        print("Random generated recipe:")
        print(response.json())
    else:
        print("Error occurred, please try again!")

# See if we can add "Tester Recipe 1", 15 minutes, Halal, and details below (Prompt 1):
def add_recipe_tester():
    new_recipe = {
        "name": "Tester Recipe 1",
        "time": 15,
        "diet": "H",
        "details": "This is a tester recipe for the purposes of running tester.py"
    }
    response = requests.post(f'{FLASK_URL}/add_recipe', json = new_recipe)
    if response.status_code == 200:
        print("New recipe added")
        print(new_recipe)
    else:
        print("Error occurred, please try again!")

# Attempt to match a user's dietary preference with a recipe from data.json (Prompt 3):
def recipes_by_diet_tester():
    diet = 'V'
    response = requests.get(f'{FLASK_URL}/recipes_by_diet/{diet}')
    if response.status_code == 200:
        print(f"Recipes for diet '{diet}':")
        print(response.json())
    else:
        print(f"Error occurred when matching '{diet}' diet, please try again!")

# This is our driver code to run the script and generate tests
if __name__ == "__main__":
    print("Begin test for Microservices successful GET / POST requests to show sending and receiving.")
    random_recipe_tester()
    add_recipe_tester()
    recipes_by_diet_tester()
