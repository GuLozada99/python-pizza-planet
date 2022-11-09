from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..common.decorators import controller_parse_data
from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)
controller = BeverageController


@beverage.route('/', methods=POST)
@controller_parse_data
def create_beverage():
    return controller.create(request.json)


@beverage.route('/', methods=PUT)
@controller_parse_data
def update_beverage():
    return controller.update(request.json)


@beverage.route('/id/<_id>', methods=GET)
@controller_parse_data
def get_beverage_by_id(_id: int):
    return controller.get_by_id(_id)


@beverage.route('/', methods=GET)
@controller_parse_data
def get_beverages():
    return controller.get_all()
