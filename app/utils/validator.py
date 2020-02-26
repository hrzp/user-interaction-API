"""
Define custom validator here
"""

from functools import wraps
from app.utils.response_handler import Response


def requirment(*data):
    """
    This decorator get some parameters and check that are they available in the data object
    if not, it will return a Response object to the client
    """
    def func_wrapper(f):
        @wraps(f)
        def returned_wrapper(*args, **kwargs):
            for param in data:
                if param not in kwargs['data']:
                    return Response.failure(f"{param} not found in data")
            return f(*args, **kwargs)
        return returned_wrapper
    return func_wrapper
