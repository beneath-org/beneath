import io
import grpc
import uuid
import json
import time
import pandas as pd
from fastavro import schemaless_writer, schemaless_reader, reader, parse_schema
from beneath.proto import gateway_pb2_grpc
from beneath.proto import gateway_pb2
from beneath.proto import engine_pb2

class Stream:
  """Stream enables read/write operations.

  Args:
    client (Client):
      Authenticator to data on Beneath.
    details (StreamDetailsResponse):
      Contains all metadata related to a Stream.
  """

  def __init__(self, client, project_name, stream_name, current_instance_id, avro_schema, batch):
    self.client = client
    self.project_name = project_name
    self.stream_name = stream_name
    self.current_instance_id = current_instance_id
    self.avro_schema = avro_schema
    self.batch = batch

  def __getstate__(self):
    return {
        "client": self.client,
        "project_name": self.project_name,
        "stream_name": self.stream_name,
        "current_instance_id": self.current_instance_id,
        "avro_schema": self.avro_schema,
        "batch": self.batch,
    }

  def __setstate__(self, obj):
    self.client = obj["client"]
    self.project_name = obj["project_name"]
    self.stream_name = obj["stream_name"]
    self.current_instance_id = obj["current_instance_id"]
    self.avro_schema = obj["avro_schema"]
    self.batch = obj["batch"]

  def read_records(self, where, limit, instance_id=None):
    # unless specified otherwise, instance_id is the current_instance_id
    if instance_id is None:
      instance_id = self.current_instance_id

    # gRPC ReadRecords from gateway
    response = self.client.stub.ReadRecords(
        gateway_pb2.ReadRecordsRequest(instance_id=instance_id, where=self._parse_where(where), limit=limit), metadata=self.client.request_metadata)

    # decode avro
    # TODO: is there a way to parallelize this? response.records is an irregular object
    # TODO: should I not be closing the _decode_avro reader every time?
    decoded_data = [0]*len(response.records)
    for i in range(len(response.records)):
      decoded_data[i] = self._decode_avro(response.records[i].avro_data)

    # return pandas dataframe
    df = pd.DataFrame(decoded_data)
    return df

  def write_record(self, instance_id, record, sequence_number=None):
    # ensure record is a dict
    if not isinstance(record, dict):
      raise TypeError("record must be a dict")

    # encode avro
    encoded_data = self._encode_avro(record)
    if sequence_number is None:
      sequence_number = int(round(time.time() * 1000))
    new_record = engine_pb2.Record(
        avro_data=encoded_data, sequence_number=sequence_number)

    # gRPC WriteRecords to gateway
    response = self.client.stub.WriteRecords(
        engine_pb2.WriteRecordsRequest(instance_id=instance_id.bytes, records=[new_record]), metadata=self.client.request_metadata)
    return response

  def _decode_avro(self, data):
    reader = io.BytesIO(data)
    record = schemaless_reader(reader, self.avro_schema)
    reader.close()
    return record

  def _encode_avro(self, record):
    writer = io.BytesIO()
    schemaless_writer(writer, self.avro_schema, record)
    result = writer.getvalue()
    writer.close()
    return result

  def _parse_where(self, where):
    if isinstance(where, str):
      return where
    elif isinstance(where, dict):
      return json.dumps(where)
    else:
      raise TypeError("expected json string or dict for parameter 'where'")