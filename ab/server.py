import time
import grpc
import positions_pb2
import positions_pb2_grpc

from concurrent import futures


class PositionService(positions_pb2_grpc.PositionServiceServicer):
    def GetPositionStream(self, request, context):
        while True:
            current_time = time.time()
            print(f"Current time: {current_time}, request: {request}")

            yield positions_pb2.PositionResponse(
                symbol=f"Current time: {current_time}",
                size=current_time,
            )
            time.sleep(1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    positions_pb2_grpc.add_PositionServiceServicer_to_server(PositionService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
