import pytest
from app.controllers import ClientController


def test_create(app, client_data: dict):
    created_client, error = ClientController.create(client_data)
    pytest.assume(error is None)
    for param, value in client_data.items():
        pytest.assume(param in created_client)
        pytest.assume(value == created_client[param])
        pytest.assume(created_client['_id'])


def test_update(app, client_data: dict):
    created_client, _ = ClientController.create(client_data)
    updated_fields = {
        'name': 'peter',
        'dni': '12123-53-6'
    }
    updated_client, error = ClientController.update({
        '_id': created_client['_id'],
        **updated_fields
    })
    pytest.assume(error is None)
    client_from_database, error = ClientController.get_by_id(
        created_client['_id'])
    pytest.assume(error is None)
    for param, value in updated_fields.items():
        pytest.assume(updated_client[param] == value)
        pytest.assume(client_from_database[param] == value)


def test_get_by_id(app, client_data: dict):
    created_client, _ = ClientController.create(client_data)
    client_from_db, error = ClientController.get_by_id(created_client['_id'])
    pytest.assume(error is None)
    for param, value in created_client.items():
        pytest.assume(client_from_db[param] == value)


def test_get_by_dni(app, client_data: dict):
    created_client, _ = ClientController.create(client_data)
    client_from_db, error = ClientController.get_by_dni(created_client['dni'])
    pytest.assume(error is None)
    for param, value in created_client.items():
        pytest.assume(client_from_db[param] == value)


def test_get_all(app, clients_data: list):
    created_clients = []
    for client in clients_data:
        created_client, _ = ClientController.create(client)
        created_clients.append(created_client)

    clients_from_db, error = ClientController.get_all()
    searchable_clients = {db_client['_id']: db_client for db_client
                     in clients_from_db}
    pytest.assume(error is None)
    for created_client in created_clients:
        current_id = created_client['_id']
        assert current_id in searchable_clients
        for param, value in created_client.items():
            pytest.assume(searchable_clients[current_id][param] == value)
