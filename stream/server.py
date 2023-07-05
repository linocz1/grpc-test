import pandas as pd
import contextvars
import time
import grpc
import asyncio
import signal

import timestamp_pb2
import timestamp_pb2_grpc

from concurrent import futures


class TimestampService(timestamp_pb2_grpc.TimestampServiceServicer):
    def __init__(self):
        pass

    async def UpdateTimestampStream(self, request_iterator, context):
        async for timestamp in request_iterator:
            print(f"Received message: {timestamp.message}, Time: {timestamp.timestamp}")

            yield timestamp_pb2.Response(result="ok")

    async def GetTimestampStream(self, request_iterator, context):
        cnt = 0
        while cnt <= 5:
            current_time = time.time()
            print(f"Current time: {current_time}")

            yield timestamp_pb2.Timestamp(
                message=f"Current time: {current_time}",
                timestamp=int(current_time),
            )
            cnt += 1

            await asyncio.sleep(1)


async def serve():
    server = grpc.aio.server()
    timestamp_pb2_grpc.add_TimestampServiceServicer_to_server(
        TimestampService(), server
    )
    server.add_insecure_port("[::]:50098")
    
    loop = asyncio.get_running_loop()

    # Register signal handler for SIGINT (KeyboardInterrupt)
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, lambda: asyncio.create_task(server.stop(0)))
    
    await server.start()
    
    await server.wait_for_termination()

if __name__ == "__main__":
    asyncio.run(serve())
