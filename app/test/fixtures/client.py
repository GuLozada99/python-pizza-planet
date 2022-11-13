import pytest

from ..utils.functions import get_random_price, get_random_string


def client_mock() -> dict:
    return {
        'address': get_random_string(),
        'dni': get_random_string(),
        'name': get_random_string(),
        'last_name': get_random_string(),
        'phone': get_random_string(),
    }


@pytest.fixture
def client_uri():
    return '/client/'


@pytest.fixture
def required_client_keys():
    return '_id', 'address', 'dni', 'name', 'last_name', 'phone'


@pytest.fixture
def client_data():
    return client_mock()


@pytest.fixture
def clients_data():
    return [client_mock() for _ in range(5)]


@pytest.fixture
def create_client(client, client_uri) -> dict:
    response = client.post(client_uri, json=client_mock())
    return response


@pytest.fixture
def create_clients(client, client_uri) -> list:
    clients = []
    for _ in range(10):
        new_client = client.post(client_uri, json=client_mock())
        clients.append(new_client.json)
    return clients
