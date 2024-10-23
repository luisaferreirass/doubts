from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pj_creater_composer import pj_creator_composer
from src.main.composer.pj_lister_composer import pj_lister_composer
from src.main.composer.pj_sacar_composer import pj_sacar_composer
from src.errors.error_handler import handler_errors

pj_routes_bp = Blueprint("pj_routes", __name__)

@pj_routes_bp.route("/pessoajuridica", methods=["POST"])
def create_pj():
    try:
        http_request = HttpRequest(body= request.json)
        view = pj_creator_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@pj_routes_bp.route("/pessoajuridica", methods=["GET"])
def list_pj():
    try:
        http_request = HttpRequest()
        view = pj_lister_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@pj_routes_bp.route("/pessoajuridica", methods=["PATCH"])
def sacar_pj():
    try:
        http_request = HttpRequest(body=request.json)
        view = pj_sacar_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_errors(exception)
        return jsonify(http_response.body), http_response.status_code
