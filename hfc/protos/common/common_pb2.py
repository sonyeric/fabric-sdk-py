# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/common/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/common/common.proto',
  package='hfc.protos.common',
  syntax='proto3',
  serialized_pb=_b('\n\x1ehfc/protos/common/common.proto\x12\x11hfc.protos.common\x1a\x1fgoogle/protobuf/timestamp.proto\"\"\n\x11LastConfiguration\x12\r\n\x05index\x18\x01 \x01(\x04\"S\n\x08Metadata\x12\r\n\x05value\x18\x01 \x01(\x0c\x12\x38\n\nsignatures\x18\x02 \x03(\x0b\x32$.hfc.protos.common.MetadataSignature\"?\n\x11MetadataSignature\x12\x17\n\x0fsignatureHeader\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"z\n\x06Header\x12\x33\n\x0b\x63hainHeader\x18\x01 \x01(\x0b\x32\x1e.hfc.protos.common.ChainHeader\x12;\n\x0fsignatureHeader\x18\x02 \x01(\x0b\x32\".hfc.protos.common.SignatureHeader\"\x9c\x01\n\x0b\x43hainHeader\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07\x63hainID\x18\x04 \x01(\t\x12\x0c\n\x04txID\x18\x05 \x01(\t\x12\r\n\x05\x65poch\x18\x06 \x01(\x04\x12\x11\n\textension\x18\x07 \x01(\x0c\"1\n\x0fSignatureHeader\x12\x0f\n\x07\x63reator\x18\x01 \x01(\x0c\x12\r\n\x05nonce\x18\x02 \x01(\x0c\"B\n\x07Payload\x12)\n\x06header\x18\x01 \x01(\x0b\x32\x19.hfc.protos.common.Header\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\".\n\x08\x45nvelope\x12\x0f\n\x07payload\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\"\x97\x01\n\x05\x42lock\x12.\n\x06Header\x18\x01 \x01(\x0b\x32\x1e.hfc.protos.common.BlockHeader\x12*\n\x04\x44\x61ta\x18\x02 \x01(\x0b\x32\x1c.hfc.protos.common.BlockData\x12\x32\n\x08Metadata\x18\x03 \x01(\x0b\x32 .hfc.protos.common.BlockMetadata\"E\n\x0b\x42lockHeader\x12\x0e\n\x06Number\x18\x01 \x01(\x04\x12\x14\n\x0cPreviousHash\x18\x02 \x01(\x0c\x12\x10\n\x08\x44\x61taHash\x18\x03 \x01(\x0c\"\x19\n\tBlockData\x12\x0c\n\x04\x44\x61ta\x18\x01 \x03(\x0c\"!\n\rBlockMetadata\x12\x10\n\x08Metadata\x18\x01 \x03(\x0c*\xaa\x01\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0c\n\x07SUCCESS\x10\xc8\x01\x12\x10\n\x0b\x42\x41\x44_REQUEST\x10\x90\x03\x12\x0e\n\tFORBIDDEN\x10\x93\x03\x12\x0e\n\tNOT_FOUND\x10\x94\x03\x12\x1d\n\x18REQUEST_ENTITY_TOO_LARGE\x10\x9d\x03\x12\x1a\n\x15INTERNAL_SERVER_ERROR\x10\xf4\x03\x12\x18\n\x13SERVICE_UNAVAILABLE\x10\xf7\x03*\x9a\x01\n\nHeaderType\x12\x0b\n\x07MESSAGE\x10\x00\x12\x1d\n\x19\x43ONFIGURATION_TRANSACTION\x10\x01\x12\x16\n\x12\x43ONFIGURATION_ITEM\x10\x02\x12\x18\n\x14\x45NDORSER_TRANSACTION\x10\x03\x12\x17\n\x13ORDERER_TRANSACTION\x10\x04\x12\x15\n\x11\x44\x45LIVER_SEEK_INFO\x10\x05*b\n\x12\x42lockMetadataIndex\x12\x0e\n\nSIGNATURES\x10\x00\x12\x16\n\x12LAST_CONFIGURATION\x10\x01\x12\x17\n\x13TRANSACTIONS_FILTER\x10\x02\x12\x0b\n\x07ORDERER\x10\x03\x42-Z+github.com/hyperledger/fabric/protos/commonb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='hfc.protos.common.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=200,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_REQUEST', index=2, number=400,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORBIDDEN', index=3, number=403,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_FOUND', index=4, number=404,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REQUEST_ENTITY_TOO_LARGE', index=5, number=413,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_SERVER_ERROR', index=6, number=500,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SERVICE_UNAVAILABLE', index=7, number=503,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1010,
  serialized_end=1180,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
_HEADERTYPE = _descriptor.EnumDescriptor(
  name='HeaderType',
  full_name='hfc.protos.common.HeaderType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MESSAGE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIGURATION_TRANSACTION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CONFIGURATION_ITEM', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENDORSER_TRANSACTION', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDERER_TRANSACTION', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELIVER_SEEK_INFO', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1183,
  serialized_end=1337,
)
_sym_db.RegisterEnumDescriptor(_HEADERTYPE)

HeaderType = enum_type_wrapper.EnumTypeWrapper(_HEADERTYPE)
_BLOCKMETADATAINDEX = _descriptor.EnumDescriptor(
  name='BlockMetadataIndex',
  full_name='hfc.protos.common.BlockMetadataIndex',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SIGNATURES', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST_CONFIGURATION', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRANSACTIONS_FILTER', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ORDERER', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1339,
  serialized_end=1437,
)
_sym_db.RegisterEnumDescriptor(_BLOCKMETADATAINDEX)

BlockMetadataIndex = enum_type_wrapper.EnumTypeWrapper(_BLOCKMETADATAINDEX)
UNKNOWN = 0
SUCCESS = 200
BAD_REQUEST = 400
FORBIDDEN = 403
NOT_FOUND = 404
REQUEST_ENTITY_TOO_LARGE = 413
INTERNAL_SERVER_ERROR = 500
SERVICE_UNAVAILABLE = 503
MESSAGE = 0
CONFIGURATION_TRANSACTION = 1
CONFIGURATION_ITEM = 2
ENDORSER_TRANSACTION = 3
ORDERER_TRANSACTION = 4
DELIVER_SEEK_INFO = 5
SIGNATURES = 0
LAST_CONFIGURATION = 1
TRANSACTIONS_FILTER = 2
ORDERER = 3



_LASTCONFIGURATION = _descriptor.Descriptor(
  name='LastConfiguration',
  full_name='hfc.protos.common.LastConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='hfc.protos.common.LastConfiguration.index', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=120,
)


_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='hfc.protos.common.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='hfc.protos.common.Metadata.value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signatures', full_name='hfc.protos.common.Metadata.signatures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=205,
)


_METADATASIGNATURE = _descriptor.Descriptor(
  name='MetadataSignature',
  full_name='hfc.protos.common.MetadataSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signatureHeader', full_name='hfc.protos.common.MetadataSignature.signatureHeader', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='hfc.protos.common.MetadataSignature.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=270,
)


_HEADER = _descriptor.Descriptor(
  name='Header',
  full_name='hfc.protos.common.Header',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chainHeader', full_name='hfc.protos.common.Header.chainHeader', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signatureHeader', full_name='hfc.protos.common.Header.signatureHeader', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=272,
  serialized_end=394,
)


_CHAINHEADER = _descriptor.Descriptor(
  name='ChainHeader',
  full_name='hfc.protos.common.ChainHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='hfc.protos.common.ChainHeader.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='hfc.protos.common.ChainHeader.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='hfc.protos.common.ChainHeader.timestamp', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chainID', full_name='hfc.protos.common.ChainHeader.chainID', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='txID', full_name='hfc.protos.common.ChainHeader.txID', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='epoch', full_name='hfc.protos.common.ChainHeader.epoch', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extension', full_name='hfc.protos.common.ChainHeader.extension', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=397,
  serialized_end=553,
)


_SIGNATUREHEADER = _descriptor.Descriptor(
  name='SignatureHeader',
  full_name='hfc.protos.common.SignatureHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creator', full_name='hfc.protos.common.SignatureHeader.creator', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nonce', full_name='hfc.protos.common.SignatureHeader.nonce', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=555,
  serialized_end=604,
)


_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='hfc.protos.common.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='hfc.protos.common.Payload.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='hfc.protos.common.Payload.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=606,
  serialized_end=672,
)


_ENVELOPE = _descriptor.Descriptor(
  name='Envelope',
  full_name='hfc.protos.common.Envelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payload', full_name='hfc.protos.common.Envelope.payload', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='signature', full_name='hfc.protos.common.Envelope.signature', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=674,
  serialized_end=720,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='hfc.protos.common.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Header', full_name='hfc.protos.common.Block.Header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Data', full_name='hfc.protos.common.Block.Data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Metadata', full_name='hfc.protos.common.Block.Metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=723,
  serialized_end=874,
)


_BLOCKHEADER = _descriptor.Descriptor(
  name='BlockHeader',
  full_name='hfc.protos.common.BlockHeader',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Number', full_name='hfc.protos.common.BlockHeader.Number', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='PreviousHash', full_name='hfc.protos.common.BlockHeader.PreviousHash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='DataHash', full_name='hfc.protos.common.BlockHeader.DataHash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=876,
  serialized_end=945,
)


_BLOCKDATA = _descriptor.Descriptor(
  name='BlockData',
  full_name='hfc.protos.common.BlockData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Data', full_name='hfc.protos.common.BlockData.Data', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=947,
  serialized_end=972,
)


_BLOCKMETADATA = _descriptor.Descriptor(
  name='BlockMetadata',
  full_name='hfc.protos.common.BlockMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Metadata', full_name='hfc.protos.common.BlockMetadata.Metadata', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=974,
  serialized_end=1007,
)

_METADATA.fields_by_name['signatures'].message_type = _METADATASIGNATURE
_HEADER.fields_by_name['chainHeader'].message_type = _CHAINHEADER
_HEADER.fields_by_name['signatureHeader'].message_type = _SIGNATUREHEADER
_CHAINHEADER.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_PAYLOAD.fields_by_name['header'].message_type = _HEADER
_BLOCK.fields_by_name['Header'].message_type = _BLOCKHEADER
_BLOCK.fields_by_name['Data'].message_type = _BLOCKDATA
_BLOCK.fields_by_name['Metadata'].message_type = _BLOCKMETADATA
DESCRIPTOR.message_types_by_name['LastConfiguration'] = _LASTCONFIGURATION
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
DESCRIPTOR.message_types_by_name['MetadataSignature'] = _METADATASIGNATURE
DESCRIPTOR.message_types_by_name['Header'] = _HEADER
DESCRIPTOR.message_types_by_name['ChainHeader'] = _CHAINHEADER
DESCRIPTOR.message_types_by_name['SignatureHeader'] = _SIGNATUREHEADER
DESCRIPTOR.message_types_by_name['Payload'] = _PAYLOAD
DESCRIPTOR.message_types_by_name['Envelope'] = _ENVELOPE
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['BlockHeader'] = _BLOCKHEADER
DESCRIPTOR.message_types_by_name['BlockData'] = _BLOCKDATA
DESCRIPTOR.message_types_by_name['BlockMetadata'] = _BLOCKMETADATA
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
DESCRIPTOR.enum_types_by_name['HeaderType'] = _HEADERTYPE
DESCRIPTOR.enum_types_by_name['BlockMetadataIndex'] = _BLOCKMETADATAINDEX

LastConfiguration = _reflection.GeneratedProtocolMessageType('LastConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _LASTCONFIGURATION,
  __module__ = 'hfc.protos.common.common_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.LastConfiguration)
  ))
_sym_db.RegisterMessage(LastConfiguration)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), dict(
  DESCRIPTOR = _METADATA,
  __module__ = 'hfc.protos.common.common_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.Metadata)
  ))
_sym_db.RegisterMessage(Metadata)

MetadataSignature = _reflection.GeneratedProtocolMessageType('MetadataSignature', (_message.Message,), dict(
  DESCRIPTOR = _METADATASIGNATURE,
  __module__ = 'hfc.protos.common.common_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.MetadataSignature)
  ))
_sym_db.RegisterMessage(MetadataSignature)

Header = _reflection.GeneratedProtocolMessageType('Header', (_message.Message,), dict(
  DESCRIPTOR = _HEADER,
  __module__ = 'hfc.protos.common.common_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.Header)
  ))
_sym_db.RegisterMessage(Header)

ChainHeader = _reflection.GeneratedProtocolMessageType('ChainHeader', (_message.Message,), dict(
  DESCRIPTOR = _CHAINHEADER,
  __module__ = 'hfc.protos.common.common_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.ChainHeader)
  ))
_sym_db.RegisterMessage(ChainHeader)

SignatureHeader = _reflection.GeneratedProtocolMessageType('SignatureHeader', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATUREHEADER,
  __module__ = 'hfc.protos.common.common_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.SignatureHeader)
  ))
_sym_db.RegisterMessage(SignatureHeader)

Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(
  DESCRIPTOR = _PAYLOAD,
  __module__ = 'hfc.protos.common.common_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.Payload)
  ))
_sym_db.RegisterMessage(Payload)

Envelope = _reflection.GeneratedProtocolMessageType('Envelope', (_message.Message,), dict(
  DESCRIPTOR = _ENVELOPE,
  __module__ = 'hfc.protos.common.common_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.Envelope)
  ))
_sym_db.RegisterMessage(Envelope)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'hfc.protos.common.common_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.Block)
  ))
_sym_db.RegisterMessage(Block)

BlockHeader = _reflection.GeneratedProtocolMessageType('BlockHeader', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKHEADER,
  __module__ = 'hfc.protos.common.common_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.BlockHeader)
  ))
_sym_db.RegisterMessage(BlockHeader)

BlockData = _reflection.GeneratedProtocolMessageType('BlockData', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKDATA,
  __module__ = 'hfc.protos.common.common_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.BlockData)
  ))
_sym_db.RegisterMessage(BlockData)

BlockMetadata = _reflection.GeneratedProtocolMessageType('BlockMetadata', (_message.Message,), dict(
  DESCRIPTOR = _BLOCKMETADATA,
  __module__ = 'hfc.protos.common.common_pb2'
  # @@protoc_insertion_point(class_scope:hfc.protos.common.BlockMetadata)
  ))
_sym_db.RegisterMessage(BlockMetadata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z+github.com/hyperledger/fabric/protos/common'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
