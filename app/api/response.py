from flask import jsonify


class ApiResponse:

    @staticmethod
    def success(data, pagination=None, status_code=200):
        response = {
            "success": True,
            "data": data,
        }
        if pagination is not None:
            response['pagination'] = {"count": pagination.get("count", 0), "page": pagination.get("page", 0)}

        return jsonify(response), status_code

    @staticmethod
    def error(message, status_code=400):
        response = {
            "success": False,
            "data": {"message": message},
        }

        return jsonify(response), status_code
