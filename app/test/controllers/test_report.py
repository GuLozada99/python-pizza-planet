from datetime import datetime

from app.controllers import ClientController, OrderController
from app.controllers.report import ReportController
from app.repositories.seeder import (create_clients, create_ingredients,
                                     create_sizes, )


def test_get_most_requested_ingredient(app):
    create_sizes()
    create_ingredients()
    create_clients(3)

    clis = [
        {'client': ClientController.get_by_id(1)[0],
         'ingredients': [1, 2, 3]},
        {'client': ClientController.get_by_id(2)[0],
         'ingredients': [1]},
        {'client': ClientController.get_by_id(3)[0],
         'ingredients': [1, 3]},
    ]

    ingredients_ids_order = [1, 3, 2]
    for _ in range(6):
        for cli in clis:
            OrderController.create({
                'size_id': 1,
                'beverages': [],
                'ingredients': cli['ingredients'],
                'client_dni': cli['client']['dni'],
            })

    most_req_ing = ReportController.get_ingredients_by_request()
    for ingredient, _id in zip(most_req_ing, ingredients_ids_order):
        assert ingredient[0]['_id'] == _id


def test_get_client_more_expenses(app):
    create_sizes()
    create_ingredients()
    create_clients(4)
    clis = [
        {'client': ClientController.get_by_id(1)[0],
         'ingredients': [1, 2, 3]},
        {'client': ClientController.get_by_id(2)[0],
         'ingredients': [1, 2]},
        {'client': ClientController.get_by_id(3)[0],
         'ingredients': [2]},
        {'client': ClientController.get_by_id(4)[0],
         'ingredients': [1, 2, 3, 4]},
    ]
    most_expenses_order = [3, 0, 1, 2]
    for _ in range(6):
        for cli in clis:
            OrderController.create({
                'size_id': 1,
                'beverages': [],
                'ingredients': cli['ingredients'],
                'client_dni': cli['client']['dni'],
            })

    clients_more_expenses = ReportController.get_clients_by_expenses()

    for client, i in zip(clients_more_expenses, most_expenses_order):
        assert clis[i]['client']['_id'] == client[0]['_id']


def test_get_months_by_revenue(app):
    create_sizes()
    create_ingredients()
    create_clients(3)

    clis = [  # months mean list of months in which client buys (1 -> Jan,
              # 2 -> Feb)
        {'client': ClientController.get_by_id(1)[0],
         'ingredients': [1, 2, 3], 'months': [1, 1, 1, 2, 3, 3]},
        {'client': ClientController.get_by_id(2)[0],
         'ingredients': [1], 'months': [1, 2]},
        {'client': ClientController.get_by_id(3)[0],
         'ingredients': [1, 3], 'months': [1, 1, 2, 2, 3, 3, 3]},
    ]

    months_most_rev = [1, 3, 2]
    for _ in range(6):
        for cli in clis:
            for month in cli['months']:
                OrderController.create({
                    'size_id': 1,
                    'date': datetime(
                        year=datetime.today().year, month=month, day=1
                    ),
                    'beverages': [],
                    'ingredients': cli['ingredients'],
                    'client_dni': cli['client']['dni'],
                })

    months_by_rev = ReportController.get_months_by_revenue()
    for month, set_month in zip(months_by_rev, months_most_rev):
        assert month[0][0] == set_month
