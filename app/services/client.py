from app.common.http_methods import GET, POST
from flask import Blueprint, request

from ..common.decorators import controller_parse_data
from ..controllers import ClientController

client = Blueprint('client', __name__)
controller = ClientController


@client.route('/', methods=POST)
@controller_parse_data
def create_client():
    return controller.create(request.json)


@client.route('/dni/<dni>', methods=GET)
@controller_parse_data
def get_client_by_dni(dni: str):
    return controller.get_by_dni(dni)
