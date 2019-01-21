from flask import Blueprint, jsonify, request

# todo: import needed packages
 # from hellomars_pb2 import HelloRequest
 # from hellomars_pb2 import HelloMars

{% for service in cookiecutter.services.buffer %}
blueprint = Blueprint("{{service.service_name}}", __name__)

@blueprint.route("{{service.options.url}}", methods=["{{service.options.method}}"])
def {{service.message_name}}():

    if request.headers.get('Content-Type') == 'application/proto':
    # your data transformation logic should go in here.
    # Business logic should be made into new modules and called from the endpoint.

        # todo: fill in input classes
        # input_msg = CurrentDemandRequest()
        # input_msg.ParseFromString(request.data)

        # Call the actual implementation method
        impl_method = {{service.options.implementation}}(input_msg)

    name = "Hugh"
    return jsonify({"msg": "Hello there, {}!".format(name or "world")})

{% endfor %}
