from app.plugins import ma
from .models import (Beverage, Client, Ingredient, OrderBeverage, Size, Order,
                     OrderDetail, )


class IngredientSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Ingredient
        load_instance = True
        fields = ('_id', 'name', 'price')


class BeverageSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Beverage
        load_instance = True
        fields = ('_id', 'name', 'price')


class SizeSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Size
        load_instance = True
        fields = ('_id', 'name', 'price')


class OrderDetailSerializer(ma.SQLAlchemyAutoSchema):

    ingredient = ma.Nested(IngredientSerializer)

    class Meta:
        model = OrderDetail
        load_instance = True
        fields = (
            'ingredient_price',
            'ingredient'
        )


class OrderBeverageSerializer(ma.SQLAlchemyAutoSchema):

    beverage = ma.Nested(BeverageSerializer)

    class Meta:
        model = OrderBeverage
        load_instance = True
        fields = (
            'beverage_price',
            'beverage'
        )


class ClientSerializer(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Client
        load_instance = True
        fields = (
            '_id',
            'name',
            'last_name',
            'dni',
            'address',
            'phone',
        )


class OrderSerializer(ma.SQLAlchemyAutoSchema):
    size = ma.Nested(SizeSerializer)
    client = ma.Nested(ClientSerializer)
    detail = ma.Nested(OrderDetailSerializer, many=True)
    beverages = ma.Nested(OrderBeverageSerializer, many=True)

    class Meta:
        model = Order
        load_instance = True
        fields = (
            '_id',
            'date',
            'total_price',
            'size',
            'client',
            'detail',
            'beverages',
        )
