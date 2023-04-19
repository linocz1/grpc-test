import time
import grpc
import timestamp_pb2
import timestamp_pb2_grpc

from concurrent import futures


class TimestampService(timestamp_pb2_grpc.TimestampServiceServicer):
    def GetTimestampStream(self, request_iterator, context):
        while True:
            current_time = time.time()
            print(f"Current time: {current_time}")

            yield timestamp_pb2.Timestamp(
                message=f"Current time: {current_time}",
                timestamp=int(current_time),
            )
            time.sleep(1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    timestamp_pb2_grpc.add_TimestampServiceServicer_to_server(TimestampService(), server)
    server.add_insecure_port("[::]:50052")
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
