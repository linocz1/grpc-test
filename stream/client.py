import grpc
import asyncio
import timestamp_pb2
import timestamp_pb2_grpc


async def run():
    async with grpc.aio.insecure_channel('localhost:50098') as channel:
        stub = timestamp_pb2_grpc.TimestampServiceStub(channel)
        try:
            async for timestamp in stub.GetTimestampStream(timestamp_pb2.Empty()):
                print(f"Received message: {timestamp.message}, Time: {timestamp.timestamp}")
        except KeyboardInterrupt:
            print("Keyboard interrupt received. Stopping program...")


if __name__ == '__main__':
    asyncio.run(run())
