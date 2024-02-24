# Sprint 2 S2.6 - Assignment 9: Microservice Implementation (Milestone #2)
# Christian McKinnon and Baorong Luo (microservice.py)
# CS 361, 2/23/2024
# This file acts as our Flask Microservice that runs on http://127.0.0.1:5000
# (Though nothing is visible here as this is a CLI-based app!)
# It directly accesses the data.json file, defines GET routes for the HTTP
# requests to and from recipes.py, and POST routes to add a new recipe entry
# to the JSON file and send a success message to the terminal.

# Imports Flask, requests for HTTP requests, json / jsonify to process data from the data.json,
# and random to generate a random recipe for the user
from flask import Flask, request, jsonify
import json
import random

micro_app = Flask(__name__)

# Load recipes from data.json and assign it to file
with open('data.json', 'r') as file:
    recipes = json.load(file)

# Here a GET request is used get a random recipe
@micro_app.route('/random_recipe', methods=['GET'])
def get_random_recipe():
    recipe = random.choice(recipes)
    # Use jsonify here to ensure data is returned in JSON format with response object
    return jsonify(recipe)

# Here a POST request is used, which appends a new recipe to the data.json file
@micro_app.route('/add_recipe', methods=['POST'])
def add_recipe():
    new_recipe = request.get_json()
    recipes.append(new_recipe)

    # Save updated recipes to data.json, using 'w' to write to the file
    with open('data.json', 'w') as file:
        json.dump(recipes, file, indent = 2)
    # Success message to print to the terminal when recipe added
    return jsonify({'message': 'Recipe added successfully'})

# Here a GET request is used get a matching recipe according to a user's dietary preferences
@micro_app.route('/recipes_by_diet/<diet>', methods=['GET'])
def get_recipes_by_diet(diet):
    matching_recipes = [recipe for recipe in recipes if recipe["diet"] == diet]
    return jsonify(matching_recipes)

# Start the Microservice with debug = True to view GET and POST requests in terminal
if __name__ == '__main__':
    micro_app.run(debug = True)
