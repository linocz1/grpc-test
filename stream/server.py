import pandas as pd
import contextvars
import time
import grpc
import asyncio

import timestamp_pb2
import timestamp_pb2_grpc

from concurrent import futures


class TimestampService(timestamp_pb2_grpc.TimestampServiceServicer):
    def __init__(self):
        pass

    async def GetTimestampStream(self, request_iterator, context):
        while True:
            current_time = time.time()
            print(f"Current time: {current_time}")

            yield timestamp_pb2.Timestamp(
                message=f"Current time: {current_time}",
                timestamp=int(current_time),
            )

            await asyncio.sleep(1)

async def serve():
    server = grpc.aio.server()
    timestamp_pb2_grpc.add_TimestampServiceServicer_to_server(TimestampService(), server)
    server.add_insecure_port("[::]:50098")
    await server.start()

    try:
        await server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    asyncio.run(serve())
