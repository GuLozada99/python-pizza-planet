import functools
from typing import Any, Callable

from flask import Response, jsonify


def controller_parse_data(f: Callable) -> Callable:
    @functools.wraps(f)
    def inner(*args: Any, **kwargs: Any) -> tuple[Response, int]:
        data, error = f(*args, **kwargs)
        response = data if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code
    return inner
