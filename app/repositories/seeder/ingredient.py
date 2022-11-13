from app.controllers import IngredientController

ingredients = [
    {'name': 'italian sausage', 'price': 4},
    {'name': 'pepperoni', 'price': 3},
    {'name': 'bacon', 'price': 4},
    {'name': 'prosciutto', 'price': 5},
    {'name': 'corn', 'price': 2},
    {'name': 'peppers and olives', 'price': 3},
    {'name': 'anchovies', 'price': 4},
    {'name': 'ruccula', 'price': 3},
    {'name': 'jam', 'price': 3},
    {'name': 'bbq chicken', 'price': 4},
]


def create_ingredients():
    if IngredientController.get_all()[0]:
        print("Ingredient table already has objects")
        return

    for ingredient in ingredients:
        IngredientController.create(ingredient)
