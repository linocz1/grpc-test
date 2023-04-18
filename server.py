import grpc
import helloworld_pb2
import helloworld_pb2_grpc

from concurrent import futures


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        message = f"Hello, {request.name}!"
        return helloworld_pb2.HelloResponse(message=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
