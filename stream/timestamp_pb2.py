# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: timestamp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftimestamp.proto\"\x07\n\x05\x45mpty\"\x1a\n\x08Response\x12\x0e\n\x06result\x18\x01 \x01(\t\"/\n\tTimestamp\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\x32r\n\x10TimestampService\x12\x32\n\x15UpdateTimestampStream\x12\n.Timestamp\x1a\t.Response(\x01\x30\x01\x12*\n\x12GetTimestampStream\x12\x06.Empty\x1a\n.Timestamp0\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'timestamp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTY._serialized_start=19
  _EMPTY._serialized_end=26
  _RESPONSE._serialized_start=28
  _RESPONSE._serialized_end=54
  _TIMESTAMP._serialized_start=56
  _TIMESTAMP._serialized_end=103
  _TIMESTAMPSERVICE._serialized_start=105
  _TIMESTAMPSERVICE._serialized_end=219
# @@protoc_insertion_point(module_scope)
