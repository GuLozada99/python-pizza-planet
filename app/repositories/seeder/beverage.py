from app.controllers import BeverageController

beverages = [
    {'name': 'pepsi', 'price': 2},
    {'name': 'coca cola', 'price': 3},
    {'name': 'iced tea', 'price': 3},
    {'name': 'lemon juice', 'price': 3},
    {'name': 'water', 'price': 1},
    {'name': 'sprite', 'price': 3},
    {'name': 'fanta', 'price': 4},
    {'name': 'sparkling water', 'price': 2},
]


def create_beverages():
    if BeverageController.get_all()[0]:
        print("Beverage table already has objects")
        return

    for beverage in beverages:
        BeverageController.create(beverage)
