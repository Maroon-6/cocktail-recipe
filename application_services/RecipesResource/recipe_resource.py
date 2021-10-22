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
    def get_by_recipe_id(cls, recipe_id):
        sql = "SELECT aa.recipe_id, aa.recipe_name, bb.quantity, dd.unit_name, cc.ingredient_name FROM " \
              "(SELECT * FROM cocktails.recipes where cocktails.recipes.recipe_id = " + recipe_id + ") AS aa " \
              "JOIN cocktails.recipe_ingredients AS bb " \
              "ON aa.recipe_id = bb.recipe_id " \
              "JOIN cocktails.ingredients AS cc " \
              "ON bb.ingredient_id = cc.ingredient_id " \
              "JOIN cocktails.units AS dd " \
              "on bb.unit_id = dd.unit_id;"

        sql_res = RDBService.run_sql(sql, None, True)
        if not sql_res:
            return None

        res = OrderedDict()
        res["recipe_id"] = sql_res[0]["recipe_id"]
        res["recipe_name"] = sql_res[0]["recipe_name"]
        res["ingredients"] = []

        for item in sql_res:
            arr = []
            if item.get("quantity", None):
                arr.append(item["quantity"])
            if item.get("unit_name", None):
                arr.append(item["unit_name"])
            if item.get("ingredient_name", None):
                arr.append(item["ingredient_name"])
            ingredient = " ".join(arr)
            if ingredient:
                res["ingredients"].append(ingredient)

        return res
