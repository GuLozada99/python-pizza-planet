from sqlalchemy import column, text

from app.repositories.managers.base import BaseManager


class IndexManager(BaseManager):

    @classmethod
    def test_connection(cls):
        cls.session.query(column('1')).from_statement(text('SELECT 1')).all()
