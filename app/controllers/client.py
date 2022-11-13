from typing import Any, Optional, Tuple

from sqlalchemy.exc import SQLAlchemyError

from ..repositories.managers import ClientManager
from .base import BaseController


class ClientController(BaseController):
    manager = ClientManager

    @classmethod
    def get_by_dni(cls, dni: str) -> Tuple[Any, Optional[str]]:
        try:
            return cls.manager.get_by_dni(dni), None
        except (SQLAlchemyError, RuntimeError) as ex:
            return None, str(ex)
