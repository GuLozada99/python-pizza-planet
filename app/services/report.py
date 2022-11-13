from app.common.http_methods import GET
from flask import Blueprint, jsonify

from ..controllers.report import ReportController

report = Blueprint('report', __name__)
controller = ReportController


@report.route('/months-by-revenue', methods=GET)
def get_months_by_revenue():
    return jsonify(controller.get_months_by_revenue())


@report.route('/ingredients-by-request', methods=GET)
def get_ingredients_by_request():
    return jsonify(controller.get_ingredients_by_request())


@report.route('/clients-by-expenses', methods=GET)
def get_clients_by_expenses():
    return jsonify(controller.get_clients_by_expenses())
