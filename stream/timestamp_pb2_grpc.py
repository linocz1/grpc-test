# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import timestamp_pb2 as timestamp__pb2


class TimestampServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateTimestampStream = channel.stream_stream(
                '/TimestampService/UpdateTimestampStream',
                request_serializer=timestamp__pb2.Timestamp.SerializeToString,
                response_deserializer=timestamp__pb2.Response.FromString,
                )
        self.GetTimestampStream = channel.unary_stream(
                '/TimestampService/GetTimestampStream',
                request_serializer=timestamp__pb2.Empty.SerializeToString,
                response_deserializer=timestamp__pb2.Timestamp.FromString,
                )


class TimestampServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpdateTimestampStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTimestampStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TimestampServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateTimestampStream': grpc.stream_stream_rpc_method_handler(
                    servicer.UpdateTimestampStream,
                    request_deserializer=timestamp__pb2.Timestamp.FromString,
                    response_serializer=timestamp__pb2.Response.SerializeToString,
            ),
            'GetTimestampStream': grpc.unary_stream_rpc_method_handler(
                    servicer.GetTimestampStream,
                    request_deserializer=timestamp__pb2.Empty.FromString,
                    response_serializer=timestamp__pb2.Timestamp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'TimestampService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TimestampService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpdateTimestampStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/TimestampService/UpdateTimestampStream',
            timestamp__pb2.Timestamp.SerializeToString,
            timestamp__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTimestampStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/TimestampService/GetTimestampStream',
            timestamp__pb2.Empty.SerializeToString,
            timestamp__pb2.Timestamp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
