"""API REST

This script allows the user to deploy API REST.
"""


import time
from os import environ 
from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.util import json_response_format

print("Libraries imported.")

app = Flask(__name__)

api_cors_config = {"origins": "*", "methods": ["GET", "POST"], "allow_headers": "*"}

CORS(app, resources={r"/*": api_cors_config})


@app.route("/api/v1/docs", methods=["GET"])
def docs():
    return "Documentation."


@app.route("/api/v1/predict", methods=["POST"])
def predict():
    data = request.json
    print(data)
    json_output = {}
    try:
        headers = request.headers
        if headers.get("X-Api-Key") is None:
            json_output_code = 401
            json_output_data_dict = {
                "response": "Ud. no se encuentra autorizado para ejecutar esta operación."
            }
            json_output = json_response_format(
                success=False,
                message="Unauthorized",
                status=json_output_code,
                data_dict=json_output_data_dict,
            )
            return jsonify(json_output), json_output_code

        auth = headers.get("X-Api-Key")
        if auth != environ.get("API_KEY"):
            json_output_code = 401
            json_output_data_dict = {"response": "Token no válido."}
            json_output = json_response_format(
                success=False,
                message="Invalid Token",
                status=json_output_code,
                data_dict=json_output_data_dict,
            )
            return jsonify(json_output), json_output_code
        
        if not data or "message" not in data:
            json_output_code = 400
            json_output_data_dict = {
                "response": "El campo 'message' es requerido."
            }
            json_output = json_response_format(
                success=False,
                message="Bad Request",
                status=json_output_code,
                data_dict=json_output_data_dict,
            )
            return jsonify(json_output), json_output_code

        initial_time = time.time()

        # TO DO

        execution_time = float(f"{(time.time() - initial_time):.06f}")
        print(f"Execution time: {execution_time:.06f} seconds")
        remote_addr = request.remote_addr
        user_agent = obtener_header(headers)

        json_output_code = 200
        json_output_data_dict = {"response": outputs}
        json_output = json_response_format(
            success=True,
            message="OK",
            status=json_output_code,
            data_dict=json_output_data_dict,
        )
    except Exception as exception_error:
        print(exception_error)
        json_output_code = 500
        json_output_data_dict = {"response": "Ha ocurrido un error."}
        json_output = json_response_format(
            success=False,
            message="Internal Server Error",
            status=json_output_code,
            data_dict=json_output_data_dict,
        )
    return jsonify(json_output), json_output_code


@app.errorhandler(404)
def handler_404(exception_error):
    print(exception_error)
    json_output_code = 404
    json_output_data_dict = {"response": "Pagina no encontrada."}
    json_output = json_response_format(
        success=False,
        message="Page not found",
        status=json_output_code,
        data_dict=json_output_data_dict,
    )
    return jsonify(json_output), json_output_code


@app.errorhandler(405)
def handler_405(exception_error):
    print(exception_error)
    json_output_code = 405
    json_output_data_dict = {
        "response": "Ud. no se encuentra autorizado para ejecutar esta operación."
    }
    json_output = json_response_format(
        success=False,
        message="The method is not allowed for the requested URL.",
        status=json_output_code,
        data_dict=json_output_data_dict,
    )
    return jsonify(json_output), json_output_code


def obtener_header(request_headers):
    user_agent = None
    if "User-Agent" in request_headers:
        user_agent = request_headers["User-Agent"]
    return user_agent


if __name__ == "__main__":
    app.run(host="0.0.0.0", load_dotenv=True)
