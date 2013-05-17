# coding=utf-8
""" Data types for sqlalchemy
"""
from __future__ import absolute_import
import json
import sqlalchemy as sa
from sqlalchemy.ext.mutable import Mutable

class MutationDict(Mutable, dict):
  """ Provides a dictionary type with mutability support.
  """
  @classmethod
  def coerce(cls, key, value):
    """Convert plain dictionaries to MutationDict."""
    if not isinstance(value, MutationDict):
      if isinstance(value, dict):
        return MutationDict(value)

      # this call will raise ValueError
      return Mutable.coerce(key, value)
    else:
      return value

  def __setitem__(self, key, value):
    """Detect dictionary set events and emit change events."""
    dict.__setitem__(self, key, value)
    self.changed()

  def __delitem__(self, key):
    """Detect dictionary del events and emit change events."""
    dict.__delitem__(self, key)
    self.changed()

  def clear(self):
    dict.clear(self)
    self.changed()

  def update(self, other):
    dict.update(self, other)
    self.changed()

  def setdefault(self, key, failobj=None):
    if not key in self.data:
        self.changed()
    return dict.setdefault(self, key, failobj)

  def pop(self, key, *args):
    self.changed()
    return dict.pop(self, key, *args)

  def popitem(self):
    self.changed()
    return dict.popitem(self)


class MutationList(Mutable, list):
  """ Provide a list type with mutability support.
  """
  @classmethod
  def coerce(cls, key, value):
    """Convert list to MutationList."""
    if not isinstance(value, MutationList):
      if isinstance(value, list):
        return MutationList(value)

      # this call will raise ValueError
      return Mutable.coerce(key, value)
    else:
      return value

  def __setitem__(self, idx, value):
    list.__setitem__(self, idx, value)
    self.changed()

  def __delitem__(self, idx):
    list.__delitem__(self, idx)
    self.changed()

  def insert(self, idx, value):
    list.insert(self, idx, value)
    self.changed()

  def __setslice__(self, i, j, other):
    list.setslice(self, i, j, other)
    self.changed()

  def __delslice__(self, i, j):
    list.delslice(self, i, j)
    self.changed()

  def __iadd__(self, other):
    l = list.iadd(self, other)
    self.changed()
    return l

  def __imul__(self, n):
    l = list.imul(self, n)
    self.changed()
    return l

  def append(self, item):
    list.append(self, item)
    self.changed()

  def pop(self, i=-1):
    item = list.pop(self, i)
    self.changed()
    return item

  def remove(self, item):
    list.remove(self, item)
    self.changed()

  def reverse(self):
    list.reverse(self)
    self.changed()

  def sort(self, *args, **kwargs):
    list.sort(self, *args, **kwargs)
    self.changed()

  def extend(self, other):
    list.extend(self, other)
    self.changed()


class JSON(sa.types.TypeDecorator):
  """Stores any structure serializable with json.

  Usage::
    JSON()
    Takes same parameters as sqlalchemy.types.Text
  """
  impl = sa.types.Text

  def process_bind_param(self, value, dialect):
    if value is not None:
      value = json.dumps(value)
    return value

  def process_result_value(self, value, dialect):
    if value is not None:
      value = json.loads(value)
    return value


def JSONDict(*args, **kwargs):
  """ Stores a dict as JSON on database, with mutability support
  """
  return MutationDict.as_mutable(JSON(*args, **kwargs))

def JSONList(*args, **kwargs):
  """ Stores a dict as JSON on database, with mutability support
  """
  return MutationList.as_mutable(JSON(*args, **kwargs))
