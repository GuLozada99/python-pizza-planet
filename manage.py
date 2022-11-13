

import pytest
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from app import flask_app
from app.plugins import db
# flake8: noqa
from app.repositories.models import (Ingredient, Order, OrderDetail, Size,
                                     Client, Beverage, OrderBeverage)
from app.repositories.seeder import (create_beverages, create_clients,
                                     create_ingredients, create_orders,
                                     create_sizes, )

manager = FlaskGroup(flask_app)

migrate = Migrate()
migrate.init_app(flask_app, db)


@manager.command('test', with_appcontext=False)
def test():
    return pytest.main(['-v', './app/test'])


@manager.command('seed', with_appcontext=True)
def seed():
    create_sizes()
    create_beverages()
    create_ingredients()
    create_clients()
    create_orders()


if __name__ == '__main__':
    manager()
