import functools
from typing import Callable

from flask import jsonify


def controller_parse_data(f: Callable):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        data, error = f(*args, **kwargs)
        response = data if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code
    return inner
