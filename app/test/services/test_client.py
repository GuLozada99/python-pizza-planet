import pytest


def test_create_client_service(create_client, required_client_keys):
    client = create_client.json
    pytest.assume(create_client.status.startswith('200'))
    for key in required_client_keys:
        pytest.assume(client[key])


def test_get_client_by_dni_service(client, create_client, client_uri):
    current_client = create_client.json
    response = client.get(f'{client_uri}dni/{current_client["dni"]}')
    pytest.assume(response.status.startswith('200'))
    returned_client = response.json
    for param, value in current_client.items():
        pytest.assume(returned_client[param] == value)
