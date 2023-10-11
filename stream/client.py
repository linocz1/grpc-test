import grpc
import time
import asyncio
import timestamp_pb2
import timestamp_pb2_grpc


async def getTimestamp():
    async with grpc.aio.insecure_channel("localhost:50098") as channel:
        stub = timestamp_pb2_grpc.TimestampServiceStub(channel)
        try:
            async for timestamp in stub.GetTimestampStream(timestamp_pb2.Empty()):
                print(
                    f"Received message: {timestamp.message}, Time: {timestamp.timestamp}"
                )
        except KeyboardInterrupt:
            print("Keyboard interrupt received. Stopping program...")


async def iterate_data():
    # Generate a stream of requests using some logic or external data source
    while True:
        # Perform necessary steps to generate the next request object
        # For example, read from a file or listen to a stream
        # Yield the request object
        timestamp = await timestampQueue.get()
        now = time.time()
        print(f"Got timestamp: {int(timestamp)}, 消耗时间: {round(now - timestamp, 3)}")

        yield timestamp_pb2.Timestamp(message=f"Hello{int(timestamp)}", timestamp=int(timestamp)),


# 每隔一秒钟向队列中添加一个时间戳
async def addTimestamp():
    while True:
        timestampQueue.put_nowait(time.time())
        await asyncio.sleep(0.001)
        


async def updateTimestamp():
    try:
        async with grpc.aio.insecure_channel("localhost:50098") as channel:
            stub = timestamp_pb2_grpc.TimestampServiceStub(channel)

            try:
                async for response in stub.UpdateTimestampStream(iterate_data()):
                    print(f"Received response: {response.result}")
            except KeyboardInterrupt:
                print("Keyboard interrupt received. Stopping program...")
    except asyncio.CancelledError:
        print("CancelledError received. Stopping program...")
    except Exception as e:
        print(f"An error occurred: {e}")


async def run():
    task1 = asyncio.create_task(getTimestamp())
    task2 = asyncio.create_task(updateTimestamp())
    task3 = asyncio.create_task(addTimestamp())

    await asyncio.gather(task1, task2, task3)


if __name__ == "__main__":
    timestampQueue = asyncio.Queue()
    asyncio.run(run())
