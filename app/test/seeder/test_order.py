import pytest

from app.controllers import OrderController
from app.repositories.seeder import (create_beverages, create_clients,
                                     create_ingredients,
                                     create_sizes, )
from app.repositories.seeder.order import create_orders, ORDERS_LENGTH


def test_create_orders(app):
    create_sizes()
    create_beverages()
    create_ingredients()
    create_clients()
    create_orders()
    db_orders, _ = OrderController.get_all()
    pytest.assume(len(db_orders) == ORDERS_LENGTH)
