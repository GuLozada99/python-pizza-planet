from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..common.decorators import controller_parse_data
from ..controllers import IngredientController

ingredient = Blueprint('ingredient', __name__)
controller = IngredientController


@ingredient.route('/', methods=POST)
@controller_parse_data
def create_ingredient():
    return controller.create(request.json)


@ingredient.route('/', methods=PUT)
@controller_parse_data
def update_ingredient():
    return controller.update(request.json)


@ingredient.route('/id/<_id>', methods=GET)
@controller_parse_data
def get_ingredient_by_id(_id: int):
    return controller.get_by_id(_id)


@ingredient.route('/', methods=GET)
@controller_parse_data
def get_ingredients():
    return controller.get_all()
