from app.common.http_methods import GET, POST
from flask import Blueprint, request

from ..common.decorators import controller_parse_data
from ..controllers import OrderController

order = Blueprint('order', __name__)
controller = OrderController


@order.route('/', methods=POST)
@controller_parse_data
def create_order():
    return controller.create(request.json)


@order.route('/id/<_id>', methods=GET)
@controller_parse_data
def get_order_by_id(_id: int):
    return controller.get_by_id(_id)


@order.route('/', methods=GET)
@controller_parse_data
def get_orders():
    return controller.get_all()
