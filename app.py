from flask import Flask, Response, request
from flask_cors import CORS
import json
import logging
from datetime import datetime

import utils.rest_utils as rest_utils

from application_services.RecipesResource.recipe_resource import RecipeResource

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

app = Flask(__name__)
CORS(app)

##################################################################################################################

# DFF TODO A real service would have more robust health check methods.
# This path simply echoes to check that the app is working.
# The path is /health and the only method is GETs
@app.route("/health", methods=["GET"])
def health_check():
    rsp_data = {"status": "healthy", "time": str(datetime.now())}
    rsp_str = json.dumps(rsp_data)
    rsp = Response(rsp_str, status=200, content_type="app/json")
    return rsp


@app.route('/')
def hello_world():
    return '<u>Hello World!</u>'


@app.route('/recipes', methods=['GET'])
def recipe_collection():
    if request.method == 'GET':
        res = RecipeResource.get_by_template(None)
        rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
        return rsp


@app.route('/recipes/<recipe_id>', methods=["GET"])
def specific_recipe(recipe_id):
    res = RecipeResource.get_by_recipe_id(recipe_id)
    rsp = Response(json.dumps(res, default=str), status=200, content_type="application/json")
    return rsp



if __name__ == '__main__':
    app.run(host="0.0.0.0")
