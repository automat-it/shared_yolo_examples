# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yolo.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nyolo.proto\";\n\x08\x42\x36\x34Image\x12\x10\n\x08\x62\x36\x34image\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\"!\n\nPrediction\x12\x13\n\x0b\x62\x36\x34response\x18\x01 \x01(\t29\n\x0eImageProcedure\x12\'\n\x0bImageMeanWH\x12\t.B64Image\x1a\x0b.Prediction\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yolo_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_B64IMAGE']._serialized_start=14
  _globals['_B64IMAGE']._serialized_end=73
  _globals['_PREDICTION']._serialized_start=75
  _globals['_PREDICTION']._serialized_end=108
  _globals['_IMAGEPROCEDURE']._serialized_start=110
  _globals['_IMAGEPROCEDURE']._serialized_end=167
# @@protoc_insertion_point(module_scope)
