import pytest

from app.controllers import ClientController
from app.repositories.seeder.client import create_clients, CLIENTS_LENGTH


def test_create_clients(app):
    create_clients()
    db_clients, _ = ClientController.get_all()
    pytest.assume(len(db_clients) == CLIENTS_LENGTH)
