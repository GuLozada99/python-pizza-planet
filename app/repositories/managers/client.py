from typing import Union

from app.repositories.managers.base import BaseManager
from app.repositories.managers.mixins import (CreateMixin, ListRetrieveMixin,
                                              UpdateMixin, )
from app.repositories.models import Client
from app.repositories.serializers import ClientSerializer


class ClientManager(BaseManager, ListRetrieveMixin, CreateMixin, UpdateMixin):
    model = Client
    serializer = ClientSerializer

    @classmethod
    def get_by_dni(cls, dni: str) -> Union[dict, None]:
        entry = cls.model.query.filter_by(dni=dni).first()
        return cls.serializer().dump(entry)
