from application_services.BaseApplicationResource import BaseRDBApplicationResource
from database_services.RDBService import RDBService
from collections import OrderedDict


class RecipeResource(BaseRDBApplicationResource):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_links(cls, resource_data):
        pass

    @classmethod
    def get_data_resource_info(cls):
        return 'cocktails', 'recipes'

    @classmethod
    def get_by_recipe_name(cls, recipe_name):
        sql_res = RDBService.find_by_template("cocktails", "recipes", {"recipe_name": recipe_name}, None)
        if not sql_res:
            return None

        res = OrderedDict()
        res["recipe_name"] = recipe_name
        res["description"] = sql_res[0]["description"]
        res["contributor"] = sql_res[0]["contributor"]
        res["ingredients"] = []

        sql_res = RDBService.find_by_template("cocktails", "recipe_ingredients", {"recipe": recipe_name}, None)

        for item in sql_res:
            if item["garnish"] and item.get("ingredient", None):
                res["ingredients"].append("Garnish by: " + item["ingredient"])
                continue
            arr = []
            if item.get("quantity", None):
                arr.append(item["quantity"])
            if item.get("unit", None):
                arr.append(item["unit"])
            if item.get("ingredient", None):
                arr.append(item["ingredient"])
            ingredient = " ".join(arr)
            if ingredient:
                res["ingredients"].append(ingredient)

        return res


    @classmethod
    def get_ingredients_by_recipe(cls, recipe_name):

        sql_res = RDBService.find_by_template("cocktails", "recipe_ingredients", {"recipe": recipe_name}, None)

        ingredients = []
        for item in sql_res:
            ingredients.append(item["ingredient"])

        return ingredients


    @classmethod
    def add_ingredient(cls, ingredient_name):
        sql_res = RDBService.find_by_template("cocktails", "ingredients", {"ingredient_name": ingredient_name}, None)
        # ingredient already exists
        if sql_res:
            return
        ingredient = {"ingredient_name": ingredient_name}
        RDBService.create("cocktails", "ingredients", ingredient)

    @classmethod
    def add_unit(cls, unit_name):
        sql_res = RDBService.find_by_template("cocktails", "units", {"unit_name": unit_name}, None)
        # ingredient already exists
        if sql_res:
            return
        unit = {"unit_name": unit_name}
        RDBService.create("cocktails", "units", unit)

    @classmethod
    def add_recipe(cls, data):
        recipe_name = data["recipe_name"]
        sql_res = RDBService.find_by_template("cocktails", "recipes", {"recipe_name": recipe_name}, None)
        # recipe already exists
        if sql_res:
            return False

        recipe = {"recipe_name": data["recipe_name"],
                  "description": data.get("description", None),
                  "contributor": data.get("contributor", None)}
        RDBService.create("cocktails", "recipes", recipe)

        for item in data["ingredients"]:
            ingredient_name = item.get("ingredient_name", None)
            if not ingredient_name:
                continue
            cls.add_ingredient(ingredient_name)
            ingredient = {"recipe": recipe_name, "ingredient": ingredient_name}
            if item.get("garnish", False):
                ingredient["garnish"] = 1
            else:
                ingredient["garnish"] = 0
                qty = item.get("quantity", None)
                if qty:
                    ingredient["quantity"] = qty
                unit = item.get("unit", None)
                if unit:
                    cls.add_unit(unit)
                    ingredient["unit"] = unit
            RDBService.create("cocktails", "recipe_ingredients", ingredient)

        return True

