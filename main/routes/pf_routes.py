from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pf_creator_composer import pf_creator_composer
from src.main.composer.pf_lister_composer import pf_lister_composer
from src.main.composer.pf_sacar_composer import pf_sacar_composer
from src.errors.error_handler import handler_errors


pf_route_bp = Blueprint("pf_routes", __name__)

@pf_route_bp.route("/pessoafisica", methods=["POST"])
def pf_create():
    try:
        http_request = HttpRequest(body= request.json)
        view = pf_creator_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_errors(exception)
        return jsonify(http_response.body), http_response.status_code
    
@pf_route_bp.route("/pessoafisica", methods=["GET"])
def pf_list():
    try:
        http_request = HttpRequest()
        view = pf_lister_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@pf_route_bp.route("/pessoafisica", methods=["PATCH"])
def pf_sacar():
    try:
        http_request = HttpRequest(body= request.json)
        view = pf_sacar_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handler_errors(exception)
        return jsonify(http_response.body), http_response.status_code

