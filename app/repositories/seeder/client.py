from faker import Faker

from app.controllers import ClientController

CLIENTS_LENGTH = 10


def create_clients():
    if ClientController.get_all()[0]:
        print("Client table already has objects")
        return

    faker = Faker()

    for _ in range(CLIENTS_LENGTH):
        ClientController.create({
            'name': faker.name(),
            'dni': faker.ssn()[:10],
            'address': faker.address(),
            'phone': faker.phone_number()[:15],
        })
