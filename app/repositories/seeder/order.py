from datetime import date, datetime, timedelta
from typing import Tuple

from faker import Faker
from faker.providers import DynamicProvider

from app.controllers import (BeverageController, ClientController,
                             IngredientController,
                             OrderController,
                             SizeController, )

ORDERS_LENGTH = 100


def get_faker() -> Faker:
    faker = Faker()
    controllers = {
        'size': SizeController,
        'ingredient': IngredientController,
        'beverage': BeverageController,
        'client': ClientController
    }
    for name, controller in controllers.items():
        items = controller.get_all()[0]
        items_provider = DynamicProvider(
            provider_name=name,
            elements=items,
        )
        faker.add_provider(items_provider)

    return faker


def create_orders(quantity: int = ORDERS_LENGTH):
    if OrderController.get_all()[0]:
        print("Order table already has objects")
        return

    faker = get_faker()
    for _ in range(quantity):
        OrderController.create({
            'client_dni': faker.client()['dni'],
            'size_id': faker.size()['_id'],
            'ingredients': [
                faker.ingredient()['_id'] for _ in range(
                    faker.pyint(max_value=5)
                )
            ],
            'beverages': [
                faker.beverage()['_id'] for _ in range(
                    faker.pyint(max_value=5)
                )
            ],
            'date': datetime(*faker.date_this_year().timetuple()[:6])
        })
