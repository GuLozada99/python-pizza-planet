from app.repositories.managers.base import BaseManager
from app.repositories.managers.mixins import (CreateMixin, ListRetrieveMixin,
                                              MultiLookupMixin,
                                              UpdateMixin, )
from app.repositories.models import Ingredient
from app.repositories.serializers import IngredientSerializer


class IngredientManager(BaseManager, ListRetrieveMixin, CreateMixin, UpdateMixin,
                        MultiLookupMixin):
    model = Ingredient
    serializer = IngredientSerializer
