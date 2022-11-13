from typing import List

from app.repositories.managers.base import BaseManager
from app.repositories.managers.mixins import ListRetrieveMixin
from app.repositories.models import (Beverage, Ingredient, Order,
                                     OrderBeverage,
                                     OrderDetail, )
from app.repositories.serializers import OrderSerializer


class OrderManager(BaseManager, ListRetrieveMixin):
    model = Order
    serializer = OrderSerializer

    @classmethod
    def create(cls, order_data: dict, ingredients: List[Ingredient], beverages: List[Beverage]):
        new_order = cls.model(**order_data)
        cls.session.add(new_order)
        cls.session.flush()
        cls.session.refresh(new_order)
        cls.session.add_all((OrderDetail(order_id=new_order._id, ingredient_id=ingredient._id, ingredient_price=ingredient.price)
                             for ingredient in ingredients))
        cls.session.add_all((OrderBeverage(order_id=new_order._id, beverage_id=beverage._id, beverage_price=beverage.price)
                             for beverage in beverages))
        cls.session.commit()
        return cls.serializer().dump(new_order)