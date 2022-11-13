from app.controllers import SizeController

sizes = [
    {'name': 'personal', 'price': 2},
    {'name': 'small', 'price': 3},
    {'name': 'medium', 'price': 5},
    {'name': 'large', 'price': 6},
    {'name': 'extra-large', 'price': 7},
]


def create_sizes():
    for size in sizes:
        SizeController.create(size)
