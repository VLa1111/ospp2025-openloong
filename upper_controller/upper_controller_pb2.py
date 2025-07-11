# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: upper_controller.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'upper_controller.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16upper_controller.proto\x12\x10upper_controller\x1a\x1bgoogle/protobuf/empty.proto\"/\n\x10\x45\x66\x66\x65\x63torPosition\x12\x0c\n\x04left\x18\x01 \x03(\x02\x12\r\n\x05right\x18\x02 \x03(\x02\"&\n\x07\x45ndPose\x12\x0c\n\x04left\x18\x01 \x03(\x02\x12\r\n\x05right\x18\x02 \x03(\x02\"*\n\x0b\x41rmPosition\x12\x0c\n\x04left\x18\x01 \x03(\x02\x12\r\n\x05right\x18\x02 \x03(\x02\"\x18\n\x08NeckPose\x12\x0c\n\x04neck\x18\x01 \x03(\x02\"\x1a\n\tWaistPose\x12\r\n\x05waist\x18\x01 \x03(\x02\"j\n\nEndPayload\x12&\n\x03\x65nd\x18\x01 \x01(\x0b\x32\x19.upper_controller.EndPose\x12\x34\n\x08\x65\x66\x66\x65\x63tor\x18\x02 \x01(\x0b\x32\".upper_controller.EffectorPosition\"n\n\nArmPayload\x12*\n\x03\x61rm\x18\x01 \x01(\x0b\x32\x1d.upper_controller.ArmPosition\x12\x34\n\x08\x65\x66\x66\x65\x63tor\x18\x02 \x01(\x0b\x32\".upper_controller.EffectorPosition\"*\n\x08Response\x12\x11\n\tsucceeded\x18\x01 \x01(\x08\x12\x0b\n\x03msg\x18\x02 \x01(\t\"}\n\x06\x43onfig\x12\x10\n\x08incharge\x18\x01 \x01(\x05\x12\x14\n\x0c\x66ilter_level\x18\x02 \x01(\x05\x12\x10\n\x08\x61rm_mode\x18\x03 \x01(\x05\x12\x12\n\ndigit_mode\x18\x04 \x01(\x05\x12\x11\n\tneck_mode\x18\x05 \x01(\x05\x12\x12\n\nwaist_mode\x18\x06 \x01(\x05\x32\xcd\x05\n\x0fUpperController\x12I\n\rsendEndAction\x12\x1c.upper_controller.EndPayload\x1a\x1a.upper_controller.Response\x12\x44\n\x0crecvEndState\x12\x16.google.protobuf.Empty\x1a\x1c.upper_controller.EndPayload\x12I\n\rsendArmAction\x12\x1c.upper_controller.ArmPayload\x1a\x1a.upper_controller.Response\x12\x44\n\x0crecvArmState\x12\x16.google.protobuf.Empty\x1a\x1c.upper_controller.ArmPayload\x12\x41\n\tsetConfig\x12\x18.upper_controller.Config\x1a\x1a.upper_controller.Response\x12=\n\tgetConfig\x12\x16.google.protobuf.Empty\x1a\x18.upper_controller.Config\x12\x45\n\x0bsetNeckPose\x12\x1a.upper_controller.NeckPose\x1a\x1a.upper_controller.Response\x12\x41\n\x0bgetNeckPose\x12\x16.google.protobuf.Empty\x1a\x1a.upper_controller.NeckPose\x12G\n\x0csetWaistPose\x12\x1b.upper_controller.WaistPose\x1a\x1a.upper_controller.Response\x12\x43\n\x0cgetWaistPose\x12\x16.google.protobuf.Empty\x1a\x1b.upper_controller.WaistPoseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'upper_controller_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EFFECTORPOSITION']._serialized_start=73
  _globals['_EFFECTORPOSITION']._serialized_end=120
  _globals['_ENDPOSE']._serialized_start=122
  _globals['_ENDPOSE']._serialized_end=160
  _globals['_ARMPOSITION']._serialized_start=162
  _globals['_ARMPOSITION']._serialized_end=204
  _globals['_NECKPOSE']._serialized_start=206
  _globals['_NECKPOSE']._serialized_end=230
  _globals['_WAISTPOSE']._serialized_start=232
  _globals['_WAISTPOSE']._serialized_end=258
  _globals['_ENDPAYLOAD']._serialized_start=260
  _globals['_ENDPAYLOAD']._serialized_end=366
  _globals['_ARMPAYLOAD']._serialized_start=368
  _globals['_ARMPAYLOAD']._serialized_end=478
  _globals['_RESPONSE']._serialized_start=480
  _globals['_RESPONSE']._serialized_end=522
  _globals['_CONFIG']._serialized_start=524
  _globals['_CONFIG']._serialized_end=649
  _globals['_UPPERCONTROLLER']._serialized_start=652
  _globals['_UPPERCONTROLLER']._serialized_end=1369
# @@protoc_insertion_point(module_scope)
