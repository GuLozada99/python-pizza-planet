from app.repositories.managers.base import BaseManager
from app.repositories.managers.mixins import (CreateMixin, ListRetrieveMixin,
                                              UpdateMixin, )
from app.repositories.models import Size
from app.repositories.serializers import SizeSerializer


class SizeManager(BaseManager, ListRetrieveMixin, CreateMixin, UpdateMixin):
    model = Size
    serializer = SizeSerializer
