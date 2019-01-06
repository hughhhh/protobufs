from flask import Blueprint, jsonify, request

blueprint = Blueprint("{{cookiecutter.blueprint_name}}", __name__)


@blueprint.route("/api/hello", methods=["GET"])
def hello_world():
    # your data transformation logic should go in here.
    # Business logic should be made into new modules and called from the endpoint.
    name = "Hugh"
    return jsonify({"msg": "Hello there, {}!".format(name or "world")})
