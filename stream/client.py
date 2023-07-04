import grpc
import asyncio
import timestamp_pb2
import timestamp_pb2_grpc

async def getTimestamp():
    async with grpc.aio.insecure_channel('localhost:50098') as channel:
        stub = timestamp_pb2_grpc.TimestampServiceStub(channel)
        try:
            async for timestamp in stub.GetTimestampStream(timestamp_pb2.Empty()):
                print(f"Received message: {timestamp.message}, Time: {timestamp.timestamp}")
        except KeyboardInterrupt:
            print("Keyboard interrupt received. Stopping program...")

async def updateTimestamp():
    async with grpc.aio.insecure_channel('localhost:50098') as channel:
        stub = timestamp_pb2_grpc.TimestampServiceStub(channel)

        # 创建请求迭代器
        requests = [
            timestamp_pb2.Timestamp(message="Hello1", timestamp=123),
            timestamp_pb2.Timestamp(message="Hello2", timestamp=456),
            timestamp_pb2.Timestamp(message="Hello3", timestamp=789),
        ]
        try:
            async for response in stub.UpdateTimestampStream(iter(requests)):
                print(f"Received response: {response.result}")
        except KeyboardInterrupt:
            print("Keyboard interrupt received. Stopping program...")


async def run():
    task1 = asyncio.create_task(getTimestamp())
    task2 = asyncio.create_task(updateTimestamp())
    
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    asyncio.run(run())

