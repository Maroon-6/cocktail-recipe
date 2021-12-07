import grequests
from datetime import datetime
import requests
import json

urls = [
    "http://127.0.0.1:5012/recipes",
    "http://127.0.0.1:5012/inventories/price"
]

# created the following apis for this service
# @app.route('/recipes/<recipe_name>/ingredients', methods=["GET"])
# @app.route('/inventories/price/<ingredient_name>', methods=["GET"])


def ingredients_of_recipe(recipe_name):
    url = urls[0] + '/' + recipe_name + '/ingredients'
    rsp = requests.get(url)
    data = json.loads(rsp.content)
    ingredients = []
    for i in data:
        ingredients.append(i)

    return ingredients


def lowest_price_of_ingredient(ingredient):
    url = process_url(ingredient)
    rsp = requests.get(url)
    data = json.loads(rsp.content)

    return data


def process_url(ingredient):
    processed = ingredient.replace(' ', '%20')
    url = urls[1] + '/' + processed

    return url


def sequential_lowest_price_recipe(recipe_name):
    s = datetime.now()
    ingredients = ingredients_of_recipe(recipe_name)
    sum = 0
    for i in ingredients:
        price = lowest_price_of_ingredient(i)
        sum += price

    e = datetime.now()

    print("sequential elapsed time = ", e - s)
    print("sequential total lowest price:", sum)
    return sum


def parallel_lowest_price_recipe(recipe_name):
    s = datetime.now()
    sum = 0

    ingredients = ingredients_of_recipe(recipe_name)
    all_url = (process_url(i) for i in ingredients)

    rs = (grequests.get(u) for u in all_url)
    x = grequests.map(rs)

    for r in x:
        sum += json.loads(r.content)
    e = datetime.now()
    print("parallel elapsed time = ", e - s)
    print("parallel total lowest price:", sum)
    return sum


# testing

recipe_n = "Cosmopolitan"

sequential_lowest_price_recipe(recipe_n)
parallel_lowest_price_recipe(recipe_n)
