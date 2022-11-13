from collections import defaultdict
from typing import Any, Dict, List, Tuple

from app.controllers import ClientController, IngredientController
from app.repositories.models import Client, Order, OrderDetail


class ReportController:

    @staticmethod
    def get_ingredients_by_request() -> List[Dict]:
        occurrences = defaultdict(lambda: 0)
        for detail in OrderDetail.query.all():
            occurrences[detail.ingredient._id] += 1

        ingredient_data = sorted(occurrences.items(), key=lambda k_v: k_v[1],
                                 reverse=True)

        return [
            {**IngredientController.get_by_id(_id)[0], 'requests': request}
            for _id, request in ingredient_data
        ]

    @staticmethod
    def get_months_by_revenue() -> List[Dict]:
        occurrences = defaultdict(lambda: 0)
        for order in Order.query.all():
            occurrences[(order.date.month, order.date.strftime('%Y'))] += \
                order.total_price

        months_data = sorted(occurrences.items(), key=lambda k_v: k_v[1],
                             reverse=True)
        return [
            {'month': date[0], 'year': date[1], 'revenue': revenue}
            for date, revenue in months_data
        ]

    @staticmethod
    def get_clients_by_expenses() -> List[Dict]:
        occurrences = defaultdict(lambda: 0)
        for client in Client.query.all():
            occurrences[client._id] += sum(order.total_price for
                                           order in client.orders)
        client_data = sorted(occurrences.items(), key=lambda k_v: k_v[1],
                             reverse=True)
        return [{**ClientController.get_by_id(_id)[0], 'expenses': expenses}
                for _id, expenses in client_data]
