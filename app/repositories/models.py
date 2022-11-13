from datetime import datetime

from sqlalchemy import UniqueConstraint

from app.plugins import db


class Order(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    total_price = db.Column(db.Float)
    size_id = db.Column(db.Integer, db.ForeignKey('size._id'))
    client_id = db.Column(db.Integer, db.ForeignKey('client._id'))

    size = db.relationship('Size', backref=db.backref('orders'))
    client = db.relationship('Client', backref=db.backref('orders'))
    detail = db.relationship('OrderDetail', backref=db.backref('orders'))
    beverages = db.relationship('OrderBeverage', backref=db.backref('orders'))


class Client(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    dni = db.Column(db.String(10))
    address = db.Column(db.String(128))
    phone = db.Column(db.String(15))
    __table_args__ = (UniqueConstraint('dni', name='unique_dni'),)


class Ingredient(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Size(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Beverage(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)


class OrderDetail(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    ingredient_price = db.Column(db.Float)
    order_id = db.Column(db.Integer, db.ForeignKey('order._id'))
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient._id'))
    ingredient = db.relationship('Ingredient', backref=db.backref('ingredient'))


class OrderBeverage(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    beverage_price = db.Column(db.Float)
    order_id = db.Column(db.Integer, db.ForeignKey('order._id'))
    beverage_id = db.Column(db.Integer, db.ForeignKey('beverage._id'))
    beverage = db.relationship('Beverage', backref=db.backref('beverage'))
