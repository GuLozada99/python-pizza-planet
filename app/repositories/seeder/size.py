from app.controllers import SizeController

sizes = [
    {'name': 'personal', 'price': 2},
    {'name': 'small', 'price': 3},
    {'name': 'medium', 'price': 5},
    {'name': 'large', 'price': 6},
    {'name': 'extra-large', 'price': 7},
]


def create_sizes():
    if SizeController.get_all()[0]:
        print("Size table already has objects")
        return

    for size in sizes:
        SizeController.create(size)
