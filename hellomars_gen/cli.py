from typing import Any, Dict
from collections import defaultdict
from cookiecutter.main import cookiecutter
from halo import Halo
from pprint import pprint

from google.protobuf.pyext._message import MethodDescriptor

# todo: Make this a param in that can be set after reading a proto
import hnd
import google.api.http_pb2
import hellomars_pb2
proto_descriptor = hellomars_pb2.DESCRIPTOR


def get_options(message: MethodDescriptor) -> Dict[str, Any]:
    """
    import my_proto_file_pb2
    value = my_proto_file_pb2.MyMessage.DESCRIPTOR.GetOptions().Extensions[my_proto_file_pb2.my_option]
    """
    # https://stackoverflow.com/questions/32836315/python-protocol-buffer-field-options
    url_path = message.GetOptions().Extensions[hnd.ext_pb2.http_options].path
    if url_path:
        print('http yes')
    else:
        raise Exception('no url path')
    method = message.GetOptions().Extensions[hnd.ext_pb2.http_options].method
    if method:
        print('method yes')
    else:
        raise Exception('no url path')
    implementation = message.GetOptions().Extensions[hnd.ext_pb2.http_options].impl
    if implementation:
        print('implementation yes')
    else:
        raise Exception('no implementation method')
    """
    Using google HTTP options for setting the path
    """
    google_http_get = message.GetOptions().Extensions[google.api.annotations_pb2.http].get
    if google_http_get:
        print('google https get yes')

    return {
        'url': url_path,
        'method': method,
        'implementation': implementation
    }


spinner = Halo(text='Loading', spinner='dots')
spinner.start()

services_map = defaultdict(list)
for k, v in proto_descriptor.services_by_name.items():
    for message in v.methods:
        service = {
            'service_name': k,
            'message_name': message.name,
            'input': message.input_type.name,
            'output': message.output_type.name,
            'options': get_options(message)
        }

    services_map['buffer'].append(service)

pprint(services_map['buffer'])
spinner.text = 'Creating a project'
cookiecutter('flask-blueprint/',
             no_input=True,
             overwrite_if_exists=True,
             extra_context={'services': services_map}) # extra context will overwrite whatever is in cookiecutter.json

# Update message on spinner
spinner.stop()
