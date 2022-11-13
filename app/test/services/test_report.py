import pytest

from app.test.utils.functions import get_random_string, get_random_price


def test_clients_by_expenses_service(get_clients_by_expenses,
                                     required_report_clients_by_expenses_keys):
    data = get_clients_by_expenses.json
    for entry in data:
        for key in required_report_clients_by_expenses_keys:
            assert entry[key]


def test_ingredients_by_request_service(
        get_ingredients_by_request,
        required_report_ingredients_by_request_keys):
    data = get_ingredients_by_request.json
    for entry in data:
        for key in required_report_ingredients_by_request_keys:
            assert entry[key]


def test_months_by_revenue_service(get_months_by_revenue,
                                   required_report_months_by_revenue_keys):
    data = get_months_by_revenue.json
    for entry in data:
        for key in required_report_months_by_revenue_keys:
            assert entry[key]
