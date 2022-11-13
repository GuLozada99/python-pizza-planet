from typing import Union

from sqlalchemy.exc import SQLAlchemyError

from ..common.utils import check_required_keys
from ..repositories.managers import (BeverageManager, ClientManager,
                                     IngredientManager,
                                     OrderManager,
                                     SizeManager, )
from .base import BaseController


class OrderController(BaseController):
    manager = OrderManager
    __required_info = ('size_id',)
    __required_info_no_client = ('client_dni', 'client_address',
                                 'client_phone', 'size_id')

    @staticmethod
    def calculate_order_price(size_price: float, ingredients: list, beverages: list):
        price = (size_price + sum(ingredient.price for ingredient in ingredients) +
                 sum(beverage.price for beverage in beverages))
        return round(price, 2)

    @classmethod
    def is_payload_valid(cls, order: dict) -> bool:
        client_dni = order.get('client_dni')
        info_to_check = cls.__required_info

        try:
            if not ClientManager.get_by_dni(client_dni):
                info_to_check = cls.__required_info_no_client
            return check_required_keys(info_to_check, order)
        except (SQLAlchemyError, RuntimeError):
            return False

    @staticmethod
    def get_client_data(order: dict) -> Union[dict, None]:
        client_dni = order.get('client_dni')

        try:
            if not (client := ClientManager.get_by_dni(client_dni)):
                client = ClientManager.create({
                    'name': order['client_name'],
                    'dni': order['client_dni'],
                    'address': order['client_address'],
                    'phone': order['client_phone'],
                })
        except (SQLAlchemyError, RuntimeError):
            client = None
        return client

    @classmethod
    def create(cls, order: dict):
        current_order = order.copy()

        if not cls.is_payload_valid(current_order):
            return 'Invalid order payload', None

        size_id = current_order.get('size_id')
        size = SizeManager.get_by_id(size_id)

        if not size:
            return 'Invalid size for Order', None

        if not (client := cls.get_client_data(current_order)):
            return 'Invalid Client data', None

        ingredient_ids = current_order.pop('ingredients', [])
        beverage_ids = current_order.pop('beverages', [])
        try:
            ingredients = IngredientManager.get_by_id_list(ingredient_ids)
            beverages = BeverageManager.get_by_id_list(beverage_ids)

            price = cls.calculate_order_price(size.get('price'),
                                              ingredients, beverages)
            order_data = {
                'size_id': current_order['size_id'],
                'client_id': client['_id'],
                'total_price': price,
                'date': current_order.get('date', None),
            }
            return cls.manager.create(order_data, ingredients, beverages), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
