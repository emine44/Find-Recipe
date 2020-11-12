import os
import requests
from seed_database import cuisine_list_in_db

url = "https://api.spoonacular.com/recipes/complexSearch"
api_key = "6cee1012c6c64927832ac09a792cf5dd"
endpoint = url + f"api_key={api_key}"

# https://api.spoonacular.com/recipes/complexSearch?apiKey=6cee1012c6c64927832ac09a792cf5dd&cuisine=german


dish_list={}
for data in cuisine_list_in_db:
    endpoint = url + f"?apiKey={api_key}&cuisine={data.cuisine_country}"
    response=requests.get(endpoint)
    dish_list[data.cuisine_country]=response.json()["results"][0]
   

