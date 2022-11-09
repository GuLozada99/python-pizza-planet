from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, request

from ..common.decorators import controller_parse_data
from ..controllers import SizeController

size = Blueprint('size', __name__)
controller = SizeController


@size.route('/', methods=POST)
@controller_parse_data
def create_size():
    return controller.create(request.json)


@size.route('/', methods=PUT)
@controller_parse_data
def update_size():
    return controller.update(request.json)


@size.route('/id/<_id>', methods=GET)
@controller_parse_data
def get_size_by_id(_id: int):
    return controller.get_by_id(_id)


@size.route('/', methods=GET)
@controller_parse_data
def get_sizes():
    return controller.get_all()
