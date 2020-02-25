"""
This class creates our response in a specific structure.
It has two static methods, a successful and failure method
Finally it returns a flask jsonify object
"""
from flask import jsonify


class Response:
    res = {
        "message": None,
        "payload": None,
        "has_error": False
    }

    @staticmethod
    def success(message=None, payload=None, status_code=200):
        Response.res["message"] = message
        Response.res["payload"] = payload
        result = jsonify(Response.res)
        result.status_code = status_code
        return result

    @staticmethod
    def failure(message=None, payload=None, status_code=400):
        Response.res["message"] = message
        Response.res["payload"] = payload
        Response.res["hasError"] = True
        result = jsonify(Response.res)
        result.status_code = status_code
        return result
