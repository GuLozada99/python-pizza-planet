import pytest

from app.controllers import IngredientController
from app.repositories.seeder.ingredient import create_ingredients, ingredients


def test_create_ingredients(app, required_ingredient_keys):
    create_ingredients()
    db_ingredients, _ = IngredientController.get_all()
    for ingredient_data, ingredient in zip(ingredients, db_ingredients):
        for key in required_ingredient_keys[1:]:
            pytest.assume(ingredient_data[key] == ingredient[key])
