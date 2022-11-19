"""API REST

Utilities module.
"""


def json_response_format(success=True, message="OK", status=200, data_dict=None):
    return {
        "success": success,
        "message": message,
        "status": status,
        "data": data_dict,
    }
