import pytest

from app.controllers import SizeController
from app.repositories.seeder.size import create_sizes, sizes


def test_create_sizes(app, required_size_keys):
    create_sizes()
    db_sizes, _ = SizeController.get_all()
    for size_data, size in zip(sizes, db_sizes):
        for key in required_size_keys[1:]:
            pytest.assume(size_data[key] == size[key])
