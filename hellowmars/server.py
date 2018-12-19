from concurrent import futures
import time
import math

import grpc

import hellomars_pb2
import hellomars_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class HelloMarsServicer(hellomars_pb2_grpc.HelloMarsServicer):
    def SayHello(self, request, context):
        return hellomars_pb2.HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hellomars_pb2_grpc.add_HelloMarsServicer_to_server(HelloMarsServicer(),
                                                       server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
