import grpc
import timestamp_pb2
import timestamp_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = timestamp_pb2_grpc.TimestampServiceStub(channel)
        try:
            for timestamp in stub.GetTimestampStream(timestamp_pb2.Empty()):
                print(f"Received message: {timestamp.message}, Time: {timestamp.timestamp}")
        except KeyboardInterrupt:
            print("Keyboard interrupt received. Stopping program...")


if __name__ == '__main__':
    run()
