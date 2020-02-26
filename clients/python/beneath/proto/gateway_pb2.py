# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: beneath/proto/gateway.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='beneath/proto/gateway.proto',
  package='gateway',
  syntax='proto3',
  serialized_options=b'Z*github.com/beneath-core/gateway/grpc/proto',
  serialized_pb=b'\n\x1b\x62\x65neath/proto/gateway.proto\x12\x07gateway\".\n\x06Record\x12\x11\n\tavro_data\x18\x01 \x01(\x0c\x12\x11\n\ttimestamp\x18\x02 \x01(\x03\"X\n\x0cQueryRequest\x12\x13\n\x0binstance_id\x18\x01 \x01(\x0c\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\x12\x0f\n\x07\x63ompact\x18\x03 \x01(\x08\x12\x12\n\npartitions\x18\x04 \x01(\x05\"?\n\rQueryResponse\x12\x16\n\x0ereplay_cursors\x18\x01 \x03(\x0c\x12\x16\n\x0e\x63hange_cursors\x18\x02 \x03(\x0c\"A\n\x0bReadRequest\x12\x13\n\x0binstance_id\x18\x01 \x01(\x0c\x12\x0e\n\x06\x63ursor\x18\x02 \x01(\x0c\x12\r\n\x05limit\x18\x03 \x01(\x05\"E\n\x0cReadResponse\x12 \n\x07records\x18\x01 \x03(\x0b\x32\x0f.gateway.Record\x12\x13\n\x0bnext_cursor\x18\x02 \x01(\x0c\"7\n\x10SubscribeRequest\x12\x13\n\x0binstance_id\x18\x01 \x01(\x0c\x12\x0e\n\x06\x63ursor\x18\x02 \x01(\x0c\"\x13\n\x11SubscribeResponse\"\"\n\x0bPeekRequest\x12\x13\n\x0binstance_id\x18\x01 \x01(\x0c\"<\n\x0cPeekResponse\x12\x15\n\rrewind_cursor\x18\x01 \x01(\x0c\x12\x15\n\rchange_cursor\x18\x02 \x01(\x0c\"m\n\x12RepartitionRequest\x12\x13\n\x0binstance_id\x18\x01 \x01(\x0c\x12\x12\n\npartitions\x18\x02 \x01(\x05\x12\x16\n\x0ereplay_cursors\x18\x03 \x03(\x0c\x12\x16\n\x0e\x63hange_cursors\x18\x04 \x03(\x0c\"E\n\x13RepartitionResponse\x12\x16\n\x0ereplay_cursors\x18\x01 \x03(\x0c\x12\x16\n\x0e\x63hange_cursors\x18\x02 \x03(\x0c\"E\n\x0cWriteRequest\x12\x13\n\x0binstance_id\x18\x01 \x01(\x0c\x12 \n\x07records\x18\x02 \x03(\x0b\x32\x0f.gateway.Record\"!\n\rWriteResponse\x12\x10\n\x08write_id\x18\x01 \x01(\x0c\"8\n\x0bPingRequest\x12\x11\n\tclient_id\x18\x01 \x01(\t\x12\x16\n\x0e\x63lient_version\x18\x02 \x01(\t\"Z\n\x0cPingResponse\x12\x15\n\rauthenticated\x18\x01 \x01(\x08\x12\x16\n\x0eversion_status\x18\x02 \x01(\t\x12\x1b\n\x13recommended_version\x18\x03 \x01(\t\"=\n\x10GetStreamRequest\x12\x14\n\x0cproject_name\x18\x01 \x01(\t\x12\x13\n\x0bstream_name\x18\x02 \x01(\t\"\xb4\x02\n\x11GetStreamResponse\x12\x12\n\nproject_id\x18\x01 \x01(\x0c\x12\x14\n\x0cproject_name\x18\x02 \x01(\t\x12\x11\n\tstream_id\x18\x03 \x01(\x0c\x12\x13\n\x0bstream_name\x18\x04 \x01(\t\x12\x1b\n\x13\x63urrent_instance_id\x18\x05 \x01(\x0c\x12\x0e\n\x06public\x18\x06 \x01(\x08\x12\x10\n\x08\x65xternal\x18\x07 \x01(\x08\x12\r\n\x05\x62\x61tch\x18\x08 \x01(\x08\x12\x0e\n\x06manual\x18\t \x01(\x08\x12\x11\n\tcommitted\x18\n \x01(\x08\x12\x19\n\x11retention_seconds\x18\x0b \x01(\x05\x12\x13\n\x0b\x61vro_schema\x18\x0c \x01(\t\x12,\n\x07indexes\x18\r \x03(\x0b\x32\x1b.gateway.StreamIndexDetails\"Z\n\x12StreamIndexDetails\x12\x10\n\x08index_id\x18\x01 \x01(\x0c\x12\x0e\n\x06\x66ields\x18\x02 \x03(\t\x12\x0f\n\x07primary\x18\x03 \x01(\x08\x12\x11\n\tnormalize\x18\x04 \x01(\x08\x32\xfc\x03\n\x07Gateway\x12\x38\n\x05Query\x12\x15.gateway.QueryRequest\x1a\x16.gateway.QueryResponse\"\x00\x12\x35\n\x04Read\x12\x14.gateway.ReadRequest\x1a\x15.gateway.ReadResponse\"\x00\x12\x46\n\tSubscribe\x12\x19.gateway.SubscribeRequest\x1a\x1a.gateway.SubscribeResponse\"\x00\x30\x01\x12\x35\n\x04Peek\x12\x14.gateway.PeekRequest\x1a\x15.gateway.PeekResponse\"\x00\x12J\n\x0bRepartition\x12\x1b.gateway.RepartitionRequest\x1a\x1c.gateway.RepartitionResponse\"\x00\x12\x38\n\x05Write\x12\x15.gateway.WriteRequest\x1a\x16.gateway.WriteResponse\"\x00\x12\x35\n\x04Ping\x12\x14.gateway.PingRequest\x1a\x15.gateway.PingResponse\"\x00\x12\x44\n\tGetStream\x12\x19.gateway.GetStreamRequest\x1a\x1a.gateway.GetStreamResponse\"\x00\x42,Z*github.com/beneath-core/gateway/grpc/protob\x06proto3'
)




_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='gateway.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='avro_data', full_name='gateway.Record.avro_data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='gateway.Record.timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=86,
)


_QUERYREQUEST = _descriptor.Descriptor(
  name='QueryRequest',
  full_name='gateway.QueryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='gateway.QueryRequest.instance_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='gateway.QueryRequest.filter', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='compact', full_name='gateway.QueryRequest.compact', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partitions', full_name='gateway.QueryRequest.partitions', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=88,
  serialized_end=176,
)


_QUERYRESPONSE = _descriptor.Descriptor(
  name='QueryResponse',
  full_name='gateway.QueryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='replay_cursors', full_name='gateway.QueryResponse.replay_cursors', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='change_cursors', full_name='gateway.QueryResponse.change_cursors', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=178,
  serialized_end=241,
)


_READREQUEST = _descriptor.Descriptor(
  name='ReadRequest',
  full_name='gateway.ReadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='gateway.ReadRequest.instance_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='gateway.ReadRequest.cursor', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limit', full_name='gateway.ReadRequest.limit', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=243,
  serialized_end=308,
)


_READRESPONSE = _descriptor.Descriptor(
  name='ReadResponse',
  full_name='gateway.ReadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='records', full_name='gateway.ReadResponse.records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_cursor', full_name='gateway.ReadResponse.next_cursor', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=310,
  serialized_end=379,
)


_SUBSCRIBEREQUEST = _descriptor.Descriptor(
  name='SubscribeRequest',
  full_name='gateway.SubscribeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='gateway.SubscribeRequest.instance_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cursor', full_name='gateway.SubscribeRequest.cursor', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=381,
  serialized_end=436,
)


_SUBSCRIBERESPONSE = _descriptor.Descriptor(
  name='SubscribeResponse',
  full_name='gateway.SubscribeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=457,
)


_PEEKREQUEST = _descriptor.Descriptor(
  name='PeekRequest',
  full_name='gateway.PeekRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='gateway.PeekRequest.instance_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=459,
  serialized_end=493,
)


_PEEKRESPONSE = _descriptor.Descriptor(
  name='PeekResponse',
  full_name='gateway.PeekResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewind_cursor', full_name='gateway.PeekResponse.rewind_cursor', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='change_cursor', full_name='gateway.PeekResponse.change_cursor', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=495,
  serialized_end=555,
)


_REPARTITIONREQUEST = _descriptor.Descriptor(
  name='RepartitionRequest',
  full_name='gateway.RepartitionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='gateway.RepartitionRequest.instance_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partitions', full_name='gateway.RepartitionRequest.partitions', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='replay_cursors', full_name='gateway.RepartitionRequest.replay_cursors', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='change_cursors', full_name='gateway.RepartitionRequest.change_cursors', index=3,
      number=4, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=557,
  serialized_end=666,
)


_REPARTITIONRESPONSE = _descriptor.Descriptor(
  name='RepartitionResponse',
  full_name='gateway.RepartitionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='replay_cursors', full_name='gateway.RepartitionResponse.replay_cursors', index=0,
      number=1, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='change_cursors', full_name='gateway.RepartitionResponse.change_cursors', index=1,
      number=2, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=668,
  serialized_end=737,
)


_WRITEREQUEST = _descriptor.Descriptor(
  name='WriteRequest',
  full_name='gateway.WriteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='gateway.WriteRequest.instance_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='records', full_name='gateway.WriteRequest.records', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=739,
  serialized_end=808,
)


_WRITERESPONSE = _descriptor.Descriptor(
  name='WriteResponse',
  full_name='gateway.WriteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='write_id', full_name='gateway.WriteResponse.write_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=810,
  serialized_end=843,
)


_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='gateway.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_id', full_name='gateway.PingRequest.client_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_version', full_name='gateway.PingRequest.client_version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=845,
  serialized_end=901,
)


_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='gateway.PingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='authenticated', full_name='gateway.PingResponse.authenticated', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version_status', full_name='gateway.PingResponse.version_status', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recommended_version', full_name='gateway.PingResponse.recommended_version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=903,
  serialized_end=993,
)


_GETSTREAMREQUEST = _descriptor.Descriptor(
  name='GetStreamRequest',
  full_name='gateway.GetStreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_name', full_name='gateway.GetStreamRequest.project_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream_name', full_name='gateway.GetStreamRequest.stream_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=995,
  serialized_end=1056,
)


_GETSTREAMRESPONSE = _descriptor.Descriptor(
  name='GetStreamResponse',
  full_name='gateway.GetStreamResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='project_id', full_name='gateway.GetStreamResponse.project_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='project_name', full_name='gateway.GetStreamResponse.project_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream_id', full_name='gateway.GetStreamResponse.stream_id', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream_name', full_name='gateway.GetStreamResponse.stream_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_instance_id', full_name='gateway.GetStreamResponse.current_instance_id', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public', full_name='gateway.GetStreamResponse.public', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='external', full_name='gateway.GetStreamResponse.external', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='batch', full_name='gateway.GetStreamResponse.batch', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manual', full_name='gateway.GetStreamResponse.manual', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='committed', full_name='gateway.GetStreamResponse.committed', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retention_seconds', full_name='gateway.GetStreamResponse.retention_seconds', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avro_schema', full_name='gateway.GetStreamResponse.avro_schema', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='indexes', full_name='gateway.GetStreamResponse.indexes', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1059,
  serialized_end=1367,
)


_STREAMINDEXDETAILS = _descriptor.Descriptor(
  name='StreamIndexDetails',
  full_name='gateway.StreamIndexDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index_id', full_name='gateway.StreamIndexDetails.index_id', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='gateway.StreamIndexDetails.fields', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primary', full_name='gateway.StreamIndexDetails.primary', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normalize', full_name='gateway.StreamIndexDetails.normalize', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1369,
  serialized_end=1459,
)

_READRESPONSE.fields_by_name['records'].message_type = _RECORD
_WRITEREQUEST.fields_by_name['records'].message_type = _RECORD
_GETSTREAMRESPONSE.fields_by_name['indexes'].message_type = _STREAMINDEXDETAILS
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['QueryRequest'] = _QUERYREQUEST
DESCRIPTOR.message_types_by_name['QueryResponse'] = _QUERYRESPONSE
DESCRIPTOR.message_types_by_name['ReadRequest'] = _READREQUEST
DESCRIPTOR.message_types_by_name['ReadResponse'] = _READRESPONSE
DESCRIPTOR.message_types_by_name['SubscribeRequest'] = _SUBSCRIBEREQUEST
DESCRIPTOR.message_types_by_name['SubscribeResponse'] = _SUBSCRIBERESPONSE
DESCRIPTOR.message_types_by_name['PeekRequest'] = _PEEKREQUEST
DESCRIPTOR.message_types_by_name['PeekResponse'] = _PEEKRESPONSE
DESCRIPTOR.message_types_by_name['RepartitionRequest'] = _REPARTITIONREQUEST
DESCRIPTOR.message_types_by_name['RepartitionResponse'] = _REPARTITIONRESPONSE
DESCRIPTOR.message_types_by_name['WriteRequest'] = _WRITEREQUEST
DESCRIPTOR.message_types_by_name['WriteResponse'] = _WRITERESPONSE
DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE
DESCRIPTOR.message_types_by_name['GetStreamRequest'] = _GETSTREAMREQUEST
DESCRIPTOR.message_types_by_name['GetStreamResponse'] = _GETSTREAMRESPONSE
DESCRIPTOR.message_types_by_name['StreamIndexDetails'] = _STREAMINDEXDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), {
  'DESCRIPTOR' : _RECORD,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.Record)
  })
_sym_db.RegisterMessage(Record)

QueryRequest = _reflection.GeneratedProtocolMessageType('QueryRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUERYREQUEST,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.QueryRequest)
  })
_sym_db.RegisterMessage(QueryRequest)

QueryResponse = _reflection.GeneratedProtocolMessageType('QueryResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUERYRESPONSE,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.QueryResponse)
  })
_sym_db.RegisterMessage(QueryResponse)

ReadRequest = _reflection.GeneratedProtocolMessageType('ReadRequest', (_message.Message,), {
  'DESCRIPTOR' : _READREQUEST,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.ReadRequest)
  })
_sym_db.RegisterMessage(ReadRequest)

ReadResponse = _reflection.GeneratedProtocolMessageType('ReadResponse', (_message.Message,), {
  'DESCRIPTOR' : _READRESPONSE,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.ReadResponse)
  })
_sym_db.RegisterMessage(ReadResponse)

SubscribeRequest = _reflection.GeneratedProtocolMessageType('SubscribeRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEREQUEST,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.SubscribeRequest)
  })
_sym_db.RegisterMessage(SubscribeRequest)

SubscribeResponse = _reflection.GeneratedProtocolMessageType('SubscribeResponse', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBERESPONSE,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.SubscribeResponse)
  })
_sym_db.RegisterMessage(SubscribeResponse)

PeekRequest = _reflection.GeneratedProtocolMessageType('PeekRequest', (_message.Message,), {
  'DESCRIPTOR' : _PEEKREQUEST,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.PeekRequest)
  })
_sym_db.RegisterMessage(PeekRequest)

PeekResponse = _reflection.GeneratedProtocolMessageType('PeekResponse', (_message.Message,), {
  'DESCRIPTOR' : _PEEKRESPONSE,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.PeekResponse)
  })
_sym_db.RegisterMessage(PeekResponse)

RepartitionRequest = _reflection.GeneratedProtocolMessageType('RepartitionRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPARTITIONREQUEST,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.RepartitionRequest)
  })
_sym_db.RegisterMessage(RepartitionRequest)

RepartitionResponse = _reflection.GeneratedProtocolMessageType('RepartitionResponse', (_message.Message,), {
  'DESCRIPTOR' : _REPARTITIONRESPONSE,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.RepartitionResponse)
  })
_sym_db.RegisterMessage(RepartitionResponse)

WriteRequest = _reflection.GeneratedProtocolMessageType('WriteRequest', (_message.Message,), {
  'DESCRIPTOR' : _WRITEREQUEST,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.WriteRequest)
  })
_sym_db.RegisterMessage(WriteRequest)

WriteResponse = _reflection.GeneratedProtocolMessageType('WriteResponse', (_message.Message,), {
  'DESCRIPTOR' : _WRITERESPONSE,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.WriteResponse)
  })
_sym_db.RegisterMessage(WriteResponse)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQUEST,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.PingRequest)
  })
_sym_db.RegisterMessage(PingRequest)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), {
  'DESCRIPTOR' : _PINGRESPONSE,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.PingResponse)
  })
_sym_db.RegisterMessage(PingResponse)

GetStreamRequest = _reflection.GeneratedProtocolMessageType('GetStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTREAMREQUEST,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetStreamRequest)
  })
_sym_db.RegisterMessage(GetStreamRequest)

GetStreamResponse = _reflection.GeneratedProtocolMessageType('GetStreamResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETSTREAMRESPONSE,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.GetStreamResponse)
  })
_sym_db.RegisterMessage(GetStreamResponse)

StreamIndexDetails = _reflection.GeneratedProtocolMessageType('StreamIndexDetails', (_message.Message,), {
  'DESCRIPTOR' : _STREAMINDEXDETAILS,
  '__module__' : 'beneath.proto.gateway_pb2'
  # @@protoc_insertion_point(class_scope:gateway.StreamIndexDetails)
  })
_sym_db.RegisterMessage(StreamIndexDetails)


DESCRIPTOR._options = None

_GATEWAY = _descriptor.ServiceDescriptor(
  name='Gateway',
  full_name='gateway.Gateway',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1462,
  serialized_end=1970,
  methods=[
  _descriptor.MethodDescriptor(
    name='Query',
    full_name='gateway.Gateway.Query',
    index=0,
    containing_service=None,
    input_type=_QUERYREQUEST,
    output_type=_QUERYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Read',
    full_name='gateway.Gateway.Read',
    index=1,
    containing_service=None,
    input_type=_READREQUEST,
    output_type=_READRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Subscribe',
    full_name='gateway.Gateway.Subscribe',
    index=2,
    containing_service=None,
    input_type=_SUBSCRIBEREQUEST,
    output_type=_SUBSCRIBERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Peek',
    full_name='gateway.Gateway.Peek',
    index=3,
    containing_service=None,
    input_type=_PEEKREQUEST,
    output_type=_PEEKRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Repartition',
    full_name='gateway.Gateway.Repartition',
    index=4,
    containing_service=None,
    input_type=_REPARTITIONREQUEST,
    output_type=_REPARTITIONRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Write',
    full_name='gateway.Gateway.Write',
    index=5,
    containing_service=None,
    input_type=_WRITEREQUEST,
    output_type=_WRITERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='gateway.Gateway.Ping',
    index=6,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetStream',
    full_name='gateway.Gateway.GetStream',
    index=7,
    containing_service=None,
    input_type=_GETSTREAMREQUEST,
    output_type=_GETSTREAMRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GATEWAY)

DESCRIPTOR.services_by_name['Gateway'] = _GATEWAY

# @@protoc_insertion_point(module_scope)
