from app.repositories.managers.base import BaseManager
from app.repositories.managers.mixins import (CreateMixin, ListRetrieveMixin,
                                              MultiLookupMixin,
                                              UpdateMixin, )
from app.repositories.models import Beverage
from app.repositories.serializers import BeverageSerializer


class BeverageManager(BaseManager, ListRetrieveMixin, CreateMixin, UpdateMixin,
                      MultiLookupMixin):
    model = Beverage
    serializer = BeverageSerializer
