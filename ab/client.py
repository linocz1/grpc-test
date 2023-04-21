import grpc
import positions_pb2
import positions_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = positions_pb2_grpc.PositionServiceStub(channel)
        try:
            for position in stub.GetPositionStream(positions_pb2.PositionRequest(symbol='1000SHIBUSDT', direction=("buy" if True else "sell"))):
                print(f"Received message: {position.symbol}, Time: {position.size}")
        except KeyboardInterrupt:
            print("Keyboard interrupt received. Stopping program...")


if __name__ == '__main__':
    run()
