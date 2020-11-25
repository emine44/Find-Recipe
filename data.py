import os
import requests
import json
import crud

API_KEY = "6cee1012c6c64927832ac09a792cf5dd"
URL = "https://api.spoonacular.com/"

# url = "https://api.spoonacular.com/recipes/complexSearch"
# api_key = "6cee1012c6c64927832ac09a792cf5dd"
# endpoint = url + f"api_key={api_key}"

# # https://api.spoonacular.com/recipes/complexSearch?apiKey=6cee1012c6c64927832ac09a792cf5dd&cuisine=german


# dish_list={}
# for data in cuisine_list_in_db:
#     endpoint = url + f"?apiKey={api_key}&cuisine={data.cuisine_country}"
#     response=requests.get(endpoint)
#     dish_list[data.cuisine_country]=response.json()["results"][0]

def get_dish_summary(dish_id):
    res = requests.get(
        f"{URL}recipes/{dish_id}/summary",
        params={"apiKey": API_KEY}
    )
    dish_data = res.json()

    return dish_data

 # GET https://api.spoonacular.com/recipes/{id}/ingredientWidget.json
 # GET https://api.spoonacular.com/recipes/{id}/equipmentWidget.json
 # GET https://api.spoonacular.com/recipes/{id}/analyzedInstructions
 # GET https://api.spoonacular.com/food/jokes/random

def get_ingredients(dish_id):
    res = requests.get(
        f"{URL}recipes/{dish_id}/ingredientWidget.json",
        params={"apiKey": API_KEY}
    )
    ingredient_data = res.json()

    return ingredient_data

def get_equipments(dish_id):
    res = requests.get(
        f"{URL}recipes/{dish_id}/equipmentWidget.json",
        params={"apiKey": API_KEY}
    )
    equipment_data = res.json()

    return equipment_data

def get_instructions(dish_id):
    res = requests.get(
        f"{URL}recipes/{dish_id}/analyzedInstructions",
        params={"apiKey": API_KEY}
    )
    inst_data = res.json()

    return inst_data

def get_joke():
    res = requests.get(
        f"{URL}food/jokes/random",
        params={"apiKey": API_KEY}
    )
    joke_data = res.json()

    return joke_data


# print(get_dish_summary(632003))