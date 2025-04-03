from flask import jsonify


class ApiResponse:

    @staticmethod
    def success(data, pagination=None, status_code=200):
        if pagination is None:
            pagination = {"count": 0, "page": 1}

        response = {
            "success": True,
            "data": data,
            "pagination": pagination
        }

        return jsonify(response), status_code

    @staticmethod
    def error(message, status_code=400):
        response = {
            "success": False,
            "data": {"message": message},
            "pagination": {"count": 0, "page": 1}
        }

        return jsonify(response), status_code
