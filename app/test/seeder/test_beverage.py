import pytest

from app.controllers import IngredientController
from app.repositories.seeder import create_beverages, beverages


def test_create_beverages(app, required_beverage_keys):
    create_beverages()
    db_beverages, _ = IngredientController.get_all()
    for beverage_data, beverage in zip(beverages, db_beverages):
        for key in required_beverage_keys[1:]:
            pytest.assume(beverage_data[key] == beverage[key])
