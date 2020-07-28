# Allows us to use Stream as a type hint without an import cycle
# pylint: disable=wrong-import-position,ungrouped-imports
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
  from beneath.stream import Stream

import uuid

from beneath import config
from beneath.cursor import Cursor
from beneath.writer import DryInstanceWriter, InstanceWriter


class StreamInstance:

  stream: Stream
  instance_id: uuid.UUID
  _admin_data: dict

  # INITIALIZATION

  def __init__(self, stream: Stream, admin_data: dict):
    self.stream = stream
    self.instance_id = uuid.UUID(hex=admin_data["streamInstanceID"])
    self._admin_data = admin_data

  # PROPERTIES

  @property
  def is_final(self):
    return self._admin_data["madeFinalOn"] is not None

  @property
  def is_primary(self):
    return self._admin_data["madePrimaryOn"] is not None

  @property
  def version(self):
    return self._admin_data["version"]

  # CONTROL PLANE

  async def update(self, make_primary=None, make_final=None):
    self._admin_data = await self.stream.client.admin.streams.update_instance(
      instance_id=self.instance_id,
      make_primary=make_primary,
      make_final=make_final,
    )
    if make_primary:
      self.stream.primary_instance = self

  # READING RECORDS

  async def query_log(self, peek: bool = False) -> Cursor:
    resp = await self.stream.client.connection.query_log(instance_id=self.instance_id, peek=peek)
    assert len(resp.replay_cursors) <= 1 and len(resp.change_cursors) <= 1
    replay = resp.replay_cursors[0] if len(resp.replay_cursors) > 0 else None
    changes = resp.change_cursors[0] if len(resp.change_cursors) > 0 else None
    return Cursor(instance=self, replay_cursor=replay, changes_cursor=changes)

  # pylint: disable=redefined-builtin
  async def query_index(self, filter: str = None) -> Cursor:
    resp = await self.stream.client.connection.query_index(instance_id=self.instance_id, filter=filter)
    assert len(resp.replay_cursors) <= 1 and len(resp.change_cursors) <= 1
    replay = resp.replay_cursors[0] if len(resp.replay_cursors) > 0 else None
    changes = resp.change_cursors[0] if len(resp.change_cursors) > 0 else None
    return Cursor(instance=self, replay_cursor=replay, changes_cursor=changes)

  # WRITING RECORDS

  def writer(self, dry=False, write_delay_ms: int = config.DEFAULT_WRITE_DELAY_MS):
    if dry:
      return DryInstanceWriter(instance=self, max_delay_ms=write_delay_ms)
    return InstanceWriter(instance=self, max_delay_ms=write_delay_ms)


class DryStreamInstance:

  stream: Stream
  instance_id: uuid.UUID

  _version: int
  _primary: bool
  _final: bool

  # INITIALIZATION

  def __init__(self, stream: Stream, version: int, primary: bool, final: bool):
    self.stream = stream
    self.instance_id = uuid.UUID(bytes=(b'\x00' * 16))
    self._version = version
    self._primary = primary
    self._final = final

  # PROPERTIES

  @property
  def is_final(self):
    return self._final

  @property
  def is_primary(self):
    return self._primary

  @property
  def version(self):
    return self._version

  # CONTROL PLANE

  async def update(self, make_primary=None, make_final=None):
    if make_primary:
      self._primary = True
    if make_final:
      self._final = True
    if make_primary:
      self.stream.primary_instance = self

  # READING RECORDS

  async def query_log(self, peek: bool = False) -> Cursor:
    raise Exception("DryStreamInstance doesn't support query_log")

  # pylint: disable=redefined-builtin
  async def query_index(self, filter: str = None) -> Cursor:
    raise Exception("DryStreamInstance doesn't support query_index")

  # WRITING RECORDS

  # pylint: disable=unused-argument
  def writer(self, dry=False, write_delay_ms: int = config.DEFAULT_WRITE_DELAY_MS):
    return DryInstanceWriter(instance=self, max_delay_ms=write_delay_ms)