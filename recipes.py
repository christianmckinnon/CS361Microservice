# Sprint 2 S2.6 - Assignment 9: Microservice Implementation (Milestone #2)
# Christian McKinnon and Baorong Luo (recipes.py)
# CS 361, 2/23/2024
# The following is a Microservice implementation that combines the use of Flask,
# HTTP requests using the Python requests library, with the combination of a JSON
# file that contains a sample list of recipes. Requests are made to the Microservice
# through the FLASK URL in recipes.py, they are received in microservice.py, where status
# messages are printed in the terminal. The requested information is then sent back
# to recipes.py in the form of a random_recipe, recipes_by_diet, or a confirmation that
# a new recipe has been added.

# Import the required libraries: requests, json, and random
import requests
import json
import random

# Define the base URL of the microservice
FLASK_URL = 'http://127.0.0.1:5000'

# This is the method to generate a random recipe (prompt 2)
def RandomRecipe():
    response = requests.get(f'{FLASK_URL}/random_recipe')
    recipe = response.json()
    return recipe

# A method to print the recipe (used in prompts 2 and 3 down below)
def PrintRecipe(recipe):
    print("Name:", recipe["name"])
    print("Time:", recipe["time"], "minutes")
    print("Diet:", recipe["diet"])
    print("Details:", recipe["details"])

# The method that corresponds to prompt 1, where a user adds a new recipe that is appended to
# the bottom of the JSON file
def AddNewRecipe(name, time, diet, details):
    new_recipe = {
        "name": name,
        "time": time,
        "diet": diet,
        "details": details
    }
    response = requests.post(f'{FLASK_URL}/add_recipe', json=new_recipe)
    if response.status_code == 200:
        print("Recipe added successfully")
    else:
        print("Failed to add recipe")

# A method that allows a user to find a recipe that matches their dietary preference,
# for example inputting "H" = Halal
def MatchingRecipe(diet):
    response = requests.get(f'{FLASK_URL}/recipes_by_diet/{diet}')
    matching_recipes = response.json()
    return matching_recipes

# CLI Menu that continually runs as long as a user return to menu, closes if "exit" is inputted
print("Welcome to Today's recipe!")
while True:
    print("Current features: ")
    print("\n")
    print("1. Share your favorite recipe with others!")
    print("2. Don't know what to cook? Get one random recipe from our database! ")
    print("3. Look up a recipe by your dietary restrictions!")
    print("\n")

    user_input = input(
        "Enter the corresponding number to select of the above options(or 'exit' to exit the program at any time): ")

    if user_input == "1":
        name = input("Enter the name of the recipe that you want to share: ")
        time = input("Enter the how long it'd cost to make this recipe(in the unit of minutes): ")
        print("'V': vegetarian, 'VG': vegan, 'H': halal, 'K': kosher, 'GF': gluten free, 'DF': dairy free")
        diet = input("Enter the dietary restriction (abbreviation) this recipe satisfies: ")
        details = input("Enter the full recipe: ")
        print("\n")
        AddNewRecipe(name, time, diet, details)
        user_input = input("Thanks for sharing! Enter 'menu' to go back to menu or 'exit' to quit the program: ")
        if user_input.lower() == "exit":
            break

    elif user_input == "2":
        recipe = RandomRecipe()
        PrintRecipe(recipe)
        user_input = input("There's one random recipe. Enter 'menu' to go back to menu or 'exit' to quit the program: ")
        if user_input.lower() == "exit":
            break

    elif user_input == "3":
        diet_search = input("What's your dietary restriction? ")
        matching_recipes = MatchingRecipe(diet_search)
        if matching_recipes:
            random_recipe = random.choice(matching_recipes)
            PrintRecipe(random_recipe)
        else:
            print("No recipes found for the given dietary restriction")

        user_input = input(
            "There's one recipe that meets the requirement. Enter 'menu' to go back to menu or 'exit' to quit the program: ")

        if user_input.lower() == "exit":
            break

    elif user_input.lower() == "exit":
        break

# Test program to demonstrate Microservice can be called and respond with data

