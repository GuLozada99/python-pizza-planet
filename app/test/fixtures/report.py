import pytest

from app.controllers.report import ReportController


@pytest.fixture
def report_uri():
    return '/report/'


@pytest.fixture
def required_report_clients_by_expenses_keys():
    return '_id', 'name', 'dni', 'address', 'phone', 'expenses'


@pytest.fixture
def required_report_ingredients_by_request_keys():
    return '_id', 'name', 'price', 'requests'


@pytest.fixture
def required_report_months_by_revenue_keys():
    return 'month', 'year', 'revenue'


@pytest.fixture
def get_clients_by_expenses(client, report_uri):
    response = client.get(f'{report_uri}clients-by-expenses')
    return response


@pytest.fixture
def get_ingredients_by_request(client, report_uri):
    response = client.get(f'{report_uri}ingredients-by-request')
    return response


@pytest.fixture
def get_months_by_revenue(client, report_uri):
    response = client.get(f'{report_uri}months-by-revenue')
    return response
